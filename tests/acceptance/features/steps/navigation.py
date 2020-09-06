from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from tests.acceptance.features.locators.home_page import HomePageLocators
from tests.acceptance.features.page_model.home_page import HomePage
from tests.acceptance.features.page_model.results_page import ResultsPage

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


@step('Homepage elements are present')
def step_impl(context):
    home_page = HomePage(context.browser)

    assert home_page.get_header_logo().is_displayed()
    assert home_page.get_categories_menu().is_displayed()
    assert home_page.get_register_button().is_displayed()


@step('Register popup is invisible')
def step_impl(context):
    WebDriverWait(context.browser, 5).until(
        EC.invisibility_of_element_located(HomePageLocators.POPUP_REGISTER)
    )


@step('I perform a search using "(.*)')
def step_impl(context, store):
    home_page = HomePage(context.browser)
    home_page.search("alienware pc", store)


@step('I get only "(.*)" results')
def step_impl(context, store):
    results_page = ResultsPage(context.browser)
    results_page.results(store)


def wait_for_element(context, locator):
    WebDriverWait(context.browser, 60).until(
        EC.visibility_of_element_located(locator)
    )

