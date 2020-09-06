from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.acceptance.locators.home_page import HomePageLocators


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://tiendamia.com/ar/'

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

    def search_amazon(self, query):
        pass

    def search_ebay(self, query):
        pass

    def search_walmart(self, query):
        pass
