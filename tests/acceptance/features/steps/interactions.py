from behave import *

from tests.acceptance.features.page_model.home_page import HomePage

use_step_matcher('re')


@step('I click on Continuar button')
def step_impl(context):
    home_page = HomePage(context.browser)
    home_page.popup_click('Covid')


@step('I click on Ya estoy registrado button')
def step_impl(context):
    home_page = HomePage(context.browser)
    home_page.popup_click('Register')
