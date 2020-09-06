from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')
CHROME_DRIVER = ChromeDriverManager().install()


@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome(CHROME_DRIVER)
    home_page = HomePage(context.browser)
    context.browser.get(home_page.url)


@step('Covid message pops up')
def step_impl(context):
    wait_for_element(context, HomePageLocators.POPUP_COVID)


@step('Register message pops up')
def step_impl(context):
    wait_for_element(context, HomePageLocators.POPUP_REGISTER)


@step('Covid popup is invisible')
def step_impl(context):
    WebDriverWait(context.browser, 5).until(
        EC.invisibility_of_element_located(HomePageLocators.POPUP_COVID)
    )


@step('Register popup is invisible')
def step_impl(context):
    WebDriverWait(context.browser, 5).until(
        EC.invisibility_of_element_located(HomePageLocators.POPUP_REGISTER)
    )


def wait_for_element(context, locator):
    WebDriverWait(context.browser, 60).until(
        EC.visibility_of_element_located(locator)
    )

