from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.PageFactory.Locators import HomePageLocators
from selenium.webdriver.common.action_chains import  ActionChains



class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


    def find_element(self, *loc):
        return self.driver.find_element(*loc)


    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)


    def find_element_wait(self, loc):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((loc))
        )
        return element


    def find_elements_wait(self, loc):
        element = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((loc))
        )
        return self.driver.find_elements(*loc)


    def send_keys(self, element, parameters):
        element.clear()
        element.send_keys(parameters)

    def doubleClick(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    def rightClick(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    def hoverOver(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

class LeftPanelSection(BasePage):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

class BookStoreApplicationPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

class ElementsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver












    




