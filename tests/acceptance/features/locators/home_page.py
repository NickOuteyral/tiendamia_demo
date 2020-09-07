from selenium.webdriver.common.by import By


class HomePageLocators:
    POPUP_COVID = By.ID, 'lightbox_covid'
    POPUP_COVID_CLOSE = By.XPATH, f".//a[.='Continuar']"
    POPUP_REGISTER = By.ID, 'registration-home-popup3'
    POPUP_REGISTER_CLOSE = By.XPATH, f".//a[.='Ya estoy registrado']"

    HEADER_LOGO = By.XPATH, './/div[@class="header-logo"]'
    CATEGORIES_MENU = By.XPATH, './/div[@class="menu-categories"]'
    REGISTER_BUTTON = By.XPATH, './/div[@class="header-registermagento"]'

    SEARCH_BAR = By.ID, 'amz'
    AMAZON_SEARCH_BUTTON = By.ID, 'button_amz'
    EBAY_SEARCH_BUTTON = By.ID, 'button_ebay'
    WALMART_SEARCH_BUTTON = By.ID, 'button_wrt'
