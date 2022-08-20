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


@given('app state is reset')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.ID, "reset_sidebar_link").click()
    driver.find_element(By.ID, "react-burger-cross-btn").click()


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


@when('user add {number} items to cart')
def step_impl(context, number):
    driver = context.driver
    # driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_description .pricebar > button").click()
    item_num = 0
    while item_num < int(number):
        selector = ".inventory_item:nth-child(" + str(item_num + 1) + ") .inventory_item_description .pricebar > button"
        driver.find_element(By.CSS_SELECTOR,
                            selector).click()
        item_num += 1


@then('there is {number} item(s)')
def step_impl(context, number):
    num = int(number)
    driver = context.driver

    items_in_cart = len(driver.find_elements(By.CSS_SELECTOR, ".cart_item"))
    assert items_in_cart == num

    # reset app state for next test cases
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.ID, "reset_sidebar_link").click()
    driver.find_element(By.ID, "react-burger-cross-btn").click()
