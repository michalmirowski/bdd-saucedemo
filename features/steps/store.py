from behave import *

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@given('user is logged in')
def step_impl(context):
    driver = context.driver
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


@given('app is reset')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.ID, "reset_sidebar_link").click()
    driver.find_element(By.ID, "react-burger-cross-btn").click()


@given('user is on "All Items" page')
def step_impl(context):
    driver = context.driver
    driver.get('https://www.saucedemo.com/inventory.html')


@when('user clicks cart icon')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()


@then('cart is opened')
def step_impl(context):
    driver = context.driver
    output_text = driver.find_element(By.CSS_SELECTOR, ".title").text
    expected_text = 'YOUR CART'

    assert output_text == expected_text


@then('cart is empty')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    no_item_shown = wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, ".cart_item")))

    assert no_item_shown


@when('user adds {number} item(s) to cart')
def step_impl(context, number):
    driver = context.driver
    counter = 0
    while counter < int(number):
        selector = ".inventory_item:nth-child(" + str(counter + 1) + ") .inventory_item_description .pricebar > button"
        driver.find_element(By.CSS_SELECTOR,
                            selector).click()
        counter += 1


@then('in the cart is {number} item(s)')
def step_impl(context, number):
    driver = context.driver
    output_number = len(driver.find_elements(By.CSS_SELECTOR, ".cart_item"))
    expected_number = int(number)

    assert output_number == expected_number

    # reset app state for next test cases
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.ID, "reset_sidebar_link").click()
    driver.find_element(By.ID, "react-burger-cross-btn").click()


@given('cart with some items is opened')
def step_impl(context):
    context.execute_steps(u'''
        Given user is on "All Items" page
        When user adds 1 item(s) to cart
         And user clicks cart icon
         Then cart is opened
    ''')


@when('user clicks "Remove" button')
def step_impl(context):
    driver = context.driver
    remove_button = driver.find_element(By.CSS_SELECTOR,
                        ".cart_list > div:last-child .cart_item_label .item_pricebar > button")
    context.response = remove_button.get_attribute("id")
    remove_button.click()

@then('item is removed')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    selector = "#" + context.response
    removed_item_not_shown = wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, selector)))

    assert removed_item_not_shown
