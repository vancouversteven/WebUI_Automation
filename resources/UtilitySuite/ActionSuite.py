from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from resources.UtilitySuite.AppConfig import UniversialParameters
from resources.PageFactory.DemoqaPageObject import HomePage
from resources.PageFactory.Locators import HomePageLocators

class UserAction():
    def __init__(self, driver):
        self.driver = driver

    def setUp_env(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(UniversialParameters.BASEURL)
        return driver

    def tearDown_env(driver):
        driver.close()
        driver.quit()

    def AccessElementPages(driver):
        # click button
        homePage = HomePage(driver)
        CategoryCards = homePage.find_elements_wait(HomePageLocators.CATEGORUCARDS)
        # Click on Elements tab
        CategoryCards[0].click()















