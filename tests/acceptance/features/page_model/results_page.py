from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.acceptance.features.locators.results_page import ResultsPageLocators
from tests.acceptance.features.page_model.base_page import BasePage


class ResultsPage(BasePage):

    def results(self, store):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(ResultsPageLocators.RESULTS)
        )

        if store == 'Amazon':
            return self.driver.find_element(*ResultsPageLocators.RESULTS_AMAZON)
        elif store == 'eBay':
            return self.driver.find_element(*ResultsPageLocators.RESULTS_EBAY)
        else:
            return self.driver.find_element(*ResultsPageLocators.RESULTS_WALMART)
