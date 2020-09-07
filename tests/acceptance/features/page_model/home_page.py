from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.acceptance.features.locators.home_page import HomePageLocators
from tests.acceptance.features.page_model.base_page import BasePage


class HomePage(BasePage):

    @property
    def url(self):
        return 'https://tiendamia.com/ar/'

    def get_header_logo(self):
        return self.driver.find_element(*HomePageLocators.HEADER_LOGO)

    def get_categories_menu(self):
        return self.driver.find_element(*HomePageLocators.CATEGORIES_MENU)

    def get_register_button(self):
        return self.driver.find_element(*HomePageLocators.REGISTER_BUTTON)

    def popup_click(self, popup):
        if popup == 'Covid':
            locator = HomePageLocators.POPUP_COVID_CLOSE
        else:
            locator = HomePageLocators.POPUP_REGISTER_CLOSE

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        )

        web_element = self.driver.find_element(*locator)

        if locator[1] == "Continuar":
            action = webdriver.common.action_chains.ActionChains(self.driver)
            action.move_to_element_with_offset(web_element, 30, 30)
            action.click()
            action.perform()
        else:
            self.driver.find_element(*locator).click()

    def search(self, query, store):
        if store == 'Amazon':
            store_locator = HomePageLocators.AMAZON_SEARCH_BUTTON
        elif store == 'eBay':
            store_locator = HomePageLocators.EBAY_SEARCH_BUTTON
        else:
            store_locator = HomePageLocators.WALMART_SEARCH_BUTTON

        self.driver.find_element(*HomePageLocators.SEARCH_BAR).send_keys(query)
        self.driver.find_element(*store_locator).click()
