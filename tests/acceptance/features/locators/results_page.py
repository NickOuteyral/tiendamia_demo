from selenium.webdriver.common.by import By


class ResultsPageLocators:
    SEARCH_BAR = By.ID, 'amz'
    AMAZON_SEARCH_BUTTON = By.ID, 'button_amz'
    EBAY_SEARCH_BUTTON = By.ID, 'button_ebay'
    WALMART_SEARCH_BUTTON = By.ID, 'button_wrt'

    RESULTS = By.XPATH, './/div[@class="tabs-main-content-container js-main-container-wrt"]'
    RESULTS_AMAZON = By.XPATH, './/div[@class="search-content" and contains(., "amazon")]'
    RESULTS_EBAY = By.XPATH, './/div[@class="search-content" and contains(., "eBay")]'
    RESULTS_WALMART = By.XPATH, './/div[@class="search-content" and contains(., "walmart")]'
