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
        When user adds 2 item(s) to cart
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


@when('user expands sort dropdown')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.CSS_SELECTOR, ".product_sort_container").click()


@when('user chooses {sort_option} option')
def step_impl(context, sort_option):
    driver = context.driver
    sort_option_dict = {"Names (A to Z)": "1", "Names (Z to A)": "2", "Price (low to high)": "3",
                        "Price (high to low)": "4"}
    selector = ".product_sort_container > option:nth-child(" + sort_option_dict[sort_option] + ")"
    driver.find_element(By.CSS_SELECTOR, selector).click()


@then('items are displayed in {order_type}')
def step_impl(context, order_type):
    driver = context.driver
    if order_type in ("alphabetical order", "reversed alphabetical order"):
        # create list of item names
        item_list = [item.text for item in driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")]
        # assertion depends on chosen sort option
        if order_type == "alphabetical order":
            assert item_list == sorted(item_list)
        elif order_type == "reversed alphabetical order":
            assert item_list == sorted(item_list, reverse=True)

    elif order_type in ("order by price (low to high)", "order by price (high to low)"):
        # create list of item prices
        item_list = [item.text for item in driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")]
        # convert prices to numbers
        item_list = [float(item[1:]) for item in item_list]
        # assertion depends on chosen sort option
        if order_type == "order by price (low to high)":
            assert item_list == sorted(item_list)
        elif order_type == "order by price (high to low)":
            assert item_list == sorted(item_list, reverse=True)


@when('user clicks "Checkout" button')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.ID, "checkout").click()


@when('user enters {first_name} as a First Name')
def step_impl(context, first_name):
    if first_name == 'NULL':
        first_name = ''
    driver = context.driver
    driver.find_element(By.ID, "first-name").send_keys(first_name)


@when('user enters {last_name} as a Last Name')
def step_impl(context, last_name):
    if last_name == 'NULL':
        last_name = ''
    driver = context.driver
    driver.find_element(By.ID, "last-name").send_keys(last_name)


@when('user enters {postal_code} as a Zip/Postal Code')
def step_impl(context, postal_code):
    if postal_code == 'NULL':
        postal_code = ''
    driver = context.driver
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)


@when('user clicks "Continue" button')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.ID, "continue").click()


@then('checkout warning is thrown: {notification}')
def step_impl(context, notification):
    driver = context.driver
    output_notification = driver.find_element(By.CSS_SELECTOR, ".error-message-container.error > h3").text

    assert output_notification == notification


@then('user stays on "Checkout: Your Information" page')
def step_impl(context):
    driver = context.driver
    output_title = driver.find_element(By.CSS_SELECTOR, ".title").text
    expected_title = 'CHECKOUT: YOUR INFORMATION'
    output_url = driver.current_url
    expected_url = 'https://www.saucedemo.com/checkout-step-one.html'

    assert output_title == expected_title
    assert output_url == expected_url


@then('user is navigated to "Checkout: Overview" page')
def step_impl(context):
    driver = context.driver
    output_title = driver.find_element(By.CSS_SELECTOR, ".title").text
    expected_title = 'CHECKOUT: OVERVIEW'
    output_url = driver.current_url
    expected_url = 'https://www.saucedemo.com/checkout-step-two.html'

    assert output_title == expected_title
    assert output_url == expected_url


@then('total is a sum of items amounts and taxes')
def step_impl(context):
    driver = context.driver

    # sum items amounts
    item_list = [item.text for item in driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")]
    item_list = [float(item[1:]) for item in item_list]
    expected_subtotal = sum(item_list)

    # capture item total from the site and convert it to number
    output_item_total = driver.find_element(By.CSS_SELECTOR, ".summary_subtotal_label").text
    output_item_total = float(output_item_total[13:])

    # verify item total
    assert output_item_total == expected_subtotal

    # calculate expected tax amount
    expected_tax = round(expected_subtotal * 0.08, 2)
    print(expected_tax)
    # capture tax amount from the site and convert it to number
    output_tax = driver.find_element(By.CSS_SELECTOR, ".summary_tax_label").text
    output_tax = float(output_tax[6:])

    # verify tax amount
    assert output_tax == expected_tax

    # calculate expected total amount
    expected_total = expected_subtotal + expected_tax

    # capture total amount from the site and convert it to number
    output_total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    output_total = float(output_total[8:])

    # verify total amount
    assert output_total == expected_total


@given('user is on "Checkout: Overview" page')
def step_impl(context):
    context.execute_steps(u'''
        Given cart with some items is opened
        When user clicks "Checkout" button
        And user enters John as a First Name
        And user enters Doe as a Last Name
        And user enters AL19YG as a Zip/Postal Code
        And user clicks "Continue" button
        ''')


@when('user clicks "Finish" button')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.ID, "finish").click()


@then('checkout is completed')
def step_impl(context):
    driver = context.driver
    output_title = driver.find_element(By.CSS_SELECTOR, ".title").text
    expected_title = 'CHECKOUT: COMPLETE!'
    output_url = driver.current_url
    expected_url = 'https://www.saucedemo.com/checkout-complete.html'

    assert output_title == expected_title
    assert output_url == expected_url
