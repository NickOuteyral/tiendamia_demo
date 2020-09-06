from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

use_step_matcher('re')
CHROME_DRIVER = ChromeDriverManager().install()


@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome(CHROME_DRIVER)
    context.browser.get('https://tiendamia.com/ar/')


@given('I wait for popup with id "(.*)"')
def step_impl(context, element_id):
    wait_for_element_id(context, element_id)


@when('I wait for popup with id "(.*)"')
def step_impl(context, element_id):
    wait_for_element_id(context, element_id)


@given('Message with id "(.*)" pops up')
def step_impl(context, element_id):
    context.browser.find_element_by_id(element_id)


@then('Message with id "(.*)" pops up')
def step_impl(context, element_id):
    context.browser.find_element_by_id(element_id)


@then('Popup with id "(.*)" is invisible')
def step_impl(context, element_id):
    WebDriverWait(context.browser, 60).until(
        EC.invisibility_of_element_located((By.ID, element_id))
    )


def wait_for_element_id(context, element_id):
    WebDriverWait(context.browser, 60).until(
        EC.visibility_of_element_located((By.ID, element_id))
    )

