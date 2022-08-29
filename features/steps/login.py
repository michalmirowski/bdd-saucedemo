from behave import *

from selenium.webdriver.common.by import By

@given('user is on Login page')
def step_impl(context):
    driver = context.driver
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()


@when('user enters {username} as Username')
def step_impl(context, username):
    if username == 'NULL':
        username = ''
    driver = context.driver
    driver.find_element(By.ID, "user-name").send_keys(username)


@when('user enters {password} as Password')
def step_impl(context, password):
    if password == 'NULL':
        password = ''
    driver = context.driver
    driver.find_element(By.ID, "password").send_keys(password)


@when('user clicks "Login" button')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.ID, "login-button").click()


@then('user is navigated to "All Items" page')
def step_impl(context):
    driver = context.driver
    output_title = driver.find_element(By.CSS_SELECTOR, ".header_secondary_container > .title").text
    expected_title = 'PRODUCTS'
    output_url = driver.current_url
    expected_url = 'https://www.saucedemo.com/inventory.html'
    assert output_title == expected_title
    assert output_url == expected_url

@then('notification {notification} is thrown')
def step_impl(context, notification):
    driver = context.driver
    output_notification = driver.find_element(By.CSS_SELECTOR, ".error-message-container.error > h3").text

    assert output_notification == notification

@then('user is not logged into the app')
def step_impl(context):
    driver = context.driver
    login_button = driver.find_element(By.ID, "login-button")
    output_url = driver.current_url
    expected_url = 'https://www.saucedemo.com/'

    assert login_button
    assert output_url == expected_url



