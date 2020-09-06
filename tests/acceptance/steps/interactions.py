from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

use_step_matcher('re')


@given('I click on element with text "(.*)"')
def step_impl(context, text):
    WebDriverWait(context.browser, 60).until(
        EC.element_to_be_clickable((By.XPATH, f".//a[.='{text}']"))
    )

    web_element = context.browser.find_element_by_xpath(f".//a[.='{text}']")

    action = webdriver.common.action_chains.ActionChains(context.browser)
    action.move_to_element_with_offset(web_element, 30, 30)
    action.click()
    action.perform()


@then('I click on element with text "(.*)"')
def step_impl(context, text):
    WebDriverWait(context.browser, 60).until(
        EC.element_to_be_clickable((By.XPATH, f".//a[.='{text}']"))
    )

    web_element = context.browser.find_element_by_xpath(f".//a[.='{text}']")

    action = webdriver.common.action_chains.ActionChains(context.browser)
    action.move_to_element_with_offset(web_element, 30, 30)
    action.click()
    action.perform()

