from behave import fixture, use_fixture
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@fixture
def driver(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.implicitly_wait(0.5)
    yield context.driver
    context.driver.quit()

def before_all(context):
    use_fixture(driver, context)
