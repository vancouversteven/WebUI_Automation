from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import resources.UtilitySuite.ActionSuite as actions
from resources.PageFactory.DemoqaPageObject import HomePage
from resources.PageFactory.Locators import HomePageLocators
from resources.UtilitySuite.AppConfig import HomePageParameters
from resources.UtilitySuite.AppConfig import LeftPanelParameters
from resources.PageFactory.DemoqaPageObject import LeftPanelSection
from resources.PageFactory.Locators import LeftPanelLocators
from resources.PageFactory.DemoqaPageObject import BookStoreApplicationPage
from resources.UtilitySuite.AppConfig import BookPageParameters
from resources.PageFactory.Locators import BookStoreApplicationPageLocators
from resources.PageFactory.DemoqaPageObject import LoginPage
from resources.PageFactory.Locators import LoginPageLocators
from resources.UtilitySuite.AppConfig import  UniversialParameters
from resources.PageFactory.DemoqaPageObject import ElementsPage
from resources.PageFactory.Locators import ElementsPageLocators
from resources.UtilitySuite.AppConfig import ElementsPageParameters
import pytest
import time
import os.path
# from os import path
# from re import search


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


class TestCase:

    def test_HomePageUI(self, record_property):
        driver = actions.UserAction.setUp_env(self)
        # Verify Elements link is displayed
        homePage = HomePage(driver)
        # Verify all six components are displayed in home page
        record_property(" Verify Category Cards size", HomePageParameters.CATEGORYCARDS_SIZE)
        CategoryCards = homePage.find_elements(*HomePageLocators.CATEGORUCARDS)
        assert len(CategoryCards) == HomePageParameters.CATEGORYCARDS_SIZE
        record_property("Verify First Category name", HomePageParameters.ELEMENTS_TEXT)
        assert CategoryCards[0].text == HomePageParameters.ELEMENTS_TEXT
        record_property("Verify Second Category name", HomePageParameters.FORMS_TEXT)
        assert CategoryCards[1].text == HomePageParameters.FORMS_TEXT
        assert CategoryCards[2].text == HomePageParameters.ALERTS_TEXT
        assert CategoryCards[3].text == HomePageParameters.WIDGETS_TEXT
        assert CategoryCards[4].text == HomePageParameters.INTERACTIONS_TEXT
        assert CategoryCards[5].text == HomePageParameters.BOOKSTOREAPPLICATION_TEXT
        # close application
        actions.UserAction.tearDown_env(driver)


    def test_BookStoreAppPageUI(self):
        driver = actions.UserAction.setUp_env(self)
        # click button
        homePage = HomePage(driver)
        CategoryCards = homePage.find_elements(*HomePageLocators.CATEGORUCARDS)
        CategoryCards[5].click()


        leftPanel = LeftPanelSection(driver)
        BookStoreApp_Login_Menu = leftPanel.find_element(*LeftPanelLocators.BookStoreApp_Login)
        BookStoreApp_BookStore_Menu = leftPanel.find_element(*LeftPanelLocators.BookStoreApp_BookStore)
        BookStoreApp_Profile_Menu = leftPanel.find_element(*LeftPanelLocators.BookStoreApp_Profile)
        BookStoreApp_BookStoreAPI_Menu = leftPanel.find_element(*LeftPanelLocators.BookStoreApp_BookStoreAPI)

        assert BookStoreApp_Login_Menu.text == LeftPanelParameters.LOGIN_MENU_TEXT
        assert BookStoreApp_BookStore_Menu.text == LeftPanelParameters.BOOKSTORE_MENU_TEXT
        assert BookStoreApp_Profile_Menu.text == LeftPanelParameters.PROFILE_MENU_TEXT
        assert BookStoreApp_BookStoreAPI_Menu.text == LeftPanelParameters.BOOKSTOREAPI_MENU_TEXT

        bookStoreAppPage = BookStoreApplicationPage(driver)
        assert bookStoreAppPage.find_element(*BookStoreApplicationPageLocators.Login_button).is_displayed() == True
        assert bookStoreAppPage.find_element(*BookStoreApplicationPageLocators.SearchBox_Input).is_displayed() == True
        assert bookStoreAppPage.find_element(*BookStoreApplicationPageLocators.TableHeader_1).text == BookPageParameters.BOOKTABLE_HEADER_1
        assert bookStoreAppPage.find_element(*BookStoreApplicationPageLocators.TableHeader_2).text == BookPageParameters.BOOKTABLE_HEADER_2
        assert bookStoreAppPage.find_element(*BookStoreApplicationPageLocators.TableHeader_3).text == BookPageParameters.BOOKTABLE_HEADER_3
        assert bookStoreAppPage.find_element(*BookStoreApplicationPageLocators.TableHeader_4).text == BookPageParameters.BOOKTABLE_HEADER_4

        # close application
        actions.UserAction.tearDown_env(driver)

    def test_SearchBook_In_BookStore(self):
        driver = actions.UserAction.setUp_env(self)
        # click button
        homePage = HomePage(driver)
        CategoryCards = homePage.find_elements(*HomePageLocators.CATEGORUCARDS)
        CategoryCards[5].click()

        #
        bookStoreAppPage = BookStoreApplicationPage(driver)
        searchbox = bookStoreAppPage.find_element(*BookStoreApplicationPageLocators.SearchBox_Input)
        bookStoreAppPage.send_keys(searchbox, BookPageParameters.SEARCH_TEXT)
        firstBookFound = bookStoreAppPage.find_element(*BookStoreApplicationPageLocators.BookName_1)
        assert firstBookFound.text == BookPageParameters.BOOKNAME


        # close application
        actions.UserAction.tearDown_env(driver)

    def test_SearchBook_NotFund(self):
        driver = actions. UserAction.setUp_env(self)
        # click button
        homePage = HomePage(driver)
        CategoryCards = homePage.find_elements(*HomePageLocators.CATEGORUCARDS)
        CategoryCards[5].click()

        bookStoreAppPage = BookStoreApplicationPage(driver)
        searchbox = bookStoreAppPage.find_element(*BookStoreApplicationPageLocators.SearchBox_Input)
        bookStoreAppPage.send_keys(searchbox, BookPageParameters.SEARCH_TEXT_NOTFOUND)
        #
        with pytest.raises(NoSuchElementException):
            firstBookFound = bookStoreAppPage.find_element(*BookStoreApplicationPageLocators.BookName_1)

        # close application
        actions.UserAction.tearDown_env(driver)

    def test_Login(self):
        driver = actions.UserAction.setUp_env(self)
        # click button
        homePage = HomePage(driver)
        CategoryCards = homePage.find_elements_wait(HomePageLocators.CATEGORUCARDS)
        CategoryCards[5].click()

        bookStoreAppPage = BookStoreApplicationPage(driver)
        login_button = bookStoreAppPage.find_element_wait(BookStoreApplicationPageLocators.Login_button)
        login_button.click()

        loginPage = LoginPage(driver)
        login_button = loginPage.find_element_wait(LoginPageLocators.Login_button)
        username_input = loginPage.find_element_wait(LoginPageLocators.UserName_Input)
        password_input = loginPage.find_element_wait(LoginPageLocators.Password_Input)
        username_input.clear()
        username_input.send_keys(UniversialParameters.USERNAME)
        password_input.clear()
        password_input.send_keys(UniversialParameters.PASSWORD)
        login_button.click()
        signedin_username = bookStoreAppPage.find_element(*BookStoreApplicationPageLocators.SIGNIN_USERNAME)
        assert signedin_username.text == UniversialParameters.USERNAME

        # close application
        actions.UserAction.tearDown_env(driver)

    def test_Elements_TextBox(self, record_property):
        driver = actions.UserAction.setUp_env(self)
        # click button
        homePage = HomePage(driver)
        CategoryCards = homePage.find_elements_wait(HomePageLocators.CATEGORUCARDS)
        # Click on Elements tab
        CategoryCards[0].click()


        elementsPage = ElementsPage(driver)
        element_menu = elementsPage.find_element_wait(ElementsPageLocators.Elements_Menu)
        textBox_menu = elementsPage.find_element_wait(ElementsPageLocators.TextBox_Menu)
        checkBox_menu = elementsPage.find_element_wait(ElementsPageLocators.CheckBox_Menu)
        radioButton_menu = elementsPage.find_element_wait(ElementsPageLocators.RadioButton_Menu)
        webTables_menu = elementsPage.find_element_wait(ElementsPageLocators.WebTables_Menu)
        buttons_menu = elementsPage.find_element_wait(ElementsPageLocators.Buttons_Menu)
        links_menu = elementsPage.find_element_wait(ElementsPageLocators.Links_Menu)
        brokenLinks_Image_menu =elementsPage.find_element_wait(ElementsPageLocators.BrokenLinks_Image_Menu)
        upload_and_download_menu = elementsPage.find_element_wait(ElementsPageLocators.UploadAndDownload_Menu)
        dynamicProperties_menu = elementsPage.find_element_wait(ElementsPageLocators.DynamicProperties_Menu)
        assert element_menu.is_displayed() == True
        assert textBox_menu.is_displayed() == True
        assert checkBox_menu.is_displayed() == True
        assert radioButton_menu.is_displayed() == True
        assert webTables_menu.is_displayed() == True
        assert buttons_menu.is_displayed() == True
        assert links_menu.is_displayed() == True
        assert brokenLinks_Image_menu.is_displayed() == True
        assert upload_and_download_menu.is_displayed() == True
        assert dynamicProperties_menu.is_displayed() == True
        record_property("Elements menu items", "TextBox, CheckBox, RadioButton, WebTable, Buttons, Links, BrokenLink_Image, Upload and Download, Dynamic Properties")

        textBox_menu.click()
        fullname = elementsPage.find_element(*ElementsPageLocators.TextBox_FullName_Input)
        email = elementsPage.find_element(*ElementsPageLocators.TextBox_Email_Input)
        current_address = elementsPage.find_element(*ElementsPageLocators.TextBox_CurrentAddress_Input)
        permanent_address = elementsPage.find_element(*ElementsPageLocators.TextBox_PermanentAddress_Input)
        submit_button = elementsPage.find_element(*ElementsPageLocators.TextBox_Submit_Button)
        assert fullname.is_displayed() == True
        assert email.is_displayed() == True
        assert current_address.is_displayed() == True
        assert permanent_address.is_displayed() == True
        assert submit_button.is_displayed() == True
        record_property("TextBox", "")

        elementsPage.send_keys(fullname, ElementsPageParameters.FULLNAME)
        elementsPage.send_keys(email, ElementsPageParameters.EMAIL)
        elementsPage.send_keys(current_address, ElementsPageParameters.CURRENTADDRESS)
        elementsPage.send_keys(permanent_address, ElementsPageParameters.CURRENTADDRESS)
        submit_button.click()

        outputs = elementsPage.find_elements_wait(ElementsPageLocators.TextBox_Outputs)
        Name = outputs[0].text
        Email = outputs[1].text
        currentAddress = outputs[2].text
        permanentAddress = outputs[3].text

        assert Name.find(ElementsPageParameters.FULLNAME) > 0
        assert Email.find(ElementsPageParameters.EMAIL) > 0
        assert currentAddress.find(ElementsPageParameters.CURRENTADDRESS) > 0
        assert permanentAddress.find(ElementsPageParameters.CURRENTADDRESS) > 0
        record_property("TextBox result", "")

        # close application
        actions.UserAction.tearDown_env(driver)


    def test_Elements_CheckBox(self, record_property):
        driver = actions.UserAction.setUp_env(self)
        # click button
        homePage = HomePage(driver)
        CategoryCards = homePage.find_elements_wait(HomePageLocators.CATEGORUCARDS)
        # Click on Elements tab
        CategoryCards[0].click()

        elementsPage = ElementsPage(driver)
        checkBox_menu = elementsPage.find_element_wait(ElementsPageLocators.CheckBox_Menu)
        assert checkBox_menu.is_displayed() == True
        checkBox_menu.click()

        home_checkbox = elementsPage.find_element_wait(ElementsPageLocators.Home_checkBox)
        home_checkbox.click()
        checkbox_result = elementsPage.find_elements_wait(ElementsPageLocators.Home_checkBox_values)
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[1].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[2].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[3].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[4].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[5].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[6].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[7].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[8].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[9].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[10].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[11].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[12].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[13].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[14].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[15].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[16].text) > 0
        assert ElementsPageParameters.HomeCheckBox_Value.find(checkbox_result[17].text) > 0
        record_property("Home CheckBox Values: ", ElementsPageParameters.HomeCheckBox_Value)

        # close application
        actions.UserAction.tearDown_env(driver)

    def test_Element_RadioButton(self, record_property):
        driver = actions.UserAction.setUp_env(self)
        # click button
        homePage = HomePage(driver)
        CategoryCards = homePage.find_elements_wait(HomePageLocators.CATEGORUCARDS)
        # Click on Elements tab
        CategoryCards[0].click()

        elementsPage = ElementsPage(driver)
        RadioButtonMenu = elementsPage.find_element_wait(ElementsPageLocators.RadioButton_Menu)
        RadioButtonMenu.click()

        YesRadioButton = elementsPage.find_element_wait(ElementsPageLocators.Yes_RadioButton)
        ImpressiveRadioButton = elementsPage.find_element_wait(ElementsPageLocators.Impressive_RadioButton)
        NoRadioButton = elementsPage.find_element_wait(ElementsPageLocators.No_RadioButton)
        assert YesRadioButton.is_displayed() == True
        assert ImpressiveRadioButton.is_displayed() == True
        assert NoRadioButton.is_displayed() == True

        YesRadioButton.click()
        RadiobuttonSelected = elementsPage.find_element_wait(ElementsPageLocators.RadioButton_Selected)
        assert RadiobuttonSelected.text.find(ElementsPageParameters.RADIOBUTTONSELECTED_YES) >0
        ImpressiveRadioButton.click()
        RadiobuttonSelected = elementsPage.find_element_wait(ElementsPageLocators.RadioButton_Selected)
        assert RadiobuttonSelected.text.find(ElementsPageParameters.RADIOBUTTONSELECTED_IMPRESSIVE)
        record_property("Element page Radio button: ", "Yes and Impressive")
        # close application
        actions.UserAction.tearDown_env(driver)


    def test_Element_WebTable(self, record_property):
        driver = actions.UserAction.setUp_env(self)
        # click button
        homePage = HomePage(driver)
        CategoryCards = homePage.find_elements_wait(HomePageLocators.CATEGORUCARDS)
        # Click on Elements tab
        CategoryCards[0].click()

        elementsPage = ElementsPage(driver)
        webTableMenu = elementsPage.find_element_wait(ElementsPageLocators.WebTables_Menu)
        webTableMenu.click()

        TableHeaders = elementsPage.find_elements_wait(ElementsPageLocators.TableHeaders)
        assert (len(TableHeaders)) == 7
        assert elementsPage.find_element_wait(ElementsPageLocators.FirstHeader).text.strip() == ElementsPageParameters.FIRSTABLEHEADER
        assert elementsPage.find_element_wait(ElementsPageLocators.SecondHeader).text.strip() == ElementsPageParameters.SECONDTABLEHEADER
        assert elementsPage.find_element_wait(ElementsPageLocators.ThirdHeader).text.strip() == ElementsPageParameters.THIRDTABLEHEADER
        assert elementsPage.find_element_wait(ElementsPageLocators.FourthHeader).text.strip() == ElementsPageParameters.FOURTHTABLEHEADER
        assert elementsPage.find_element_wait(ElementsPageLocators.FifthHeader).text.strip() == ElementsPageParameters.FIFTHTABLEHEADER
        assert elementsPage.find_element_wait(ElementsPageLocators.SixthHeader).text.strip() == ElementsPageParameters.SIXTHTABLEHEADER
        assert elementsPage.find_element_wait(ElementsPageLocators.SeventhHeader).text.strip() == ElementsPageParameters.SEVENTHTABLEHEADER

        assert elementsPage.find_element_wait(ElementsPageLocators.Row1Cell1).text.strip() == ElementsPageParameters.R1C1
        assert elementsPage.find_element_wait(ElementsPageLocators.Row1Cell2).text.strip() == ElementsPageParameters.R1C2
        assert elementsPage.find_element_wait(ElementsPageLocators.Row1Cell3).text.strip() == ElementsPageParameters.R1C3
        assert elementsPage.find_element_wait(ElementsPageLocators.Row1Cell4).text.strip() == ElementsPageParameters.R1C4
        assert elementsPage.find_element_wait(ElementsPageLocators.Row1Cell5).text.strip() == ElementsPageParameters.R1C5
        assert elementsPage.find_element_wait(ElementsPageLocators.Row1Cell6).text.strip() == ElementsPageParameters.R1C6
        assert elementsPage.find_element_wait(ElementsPageLocators.Row1Cell7_Edit).get_attribute("title") == ElementsPageParameters.TableCell_EditTooltip
        assert elementsPage.find_element_wait(ElementsPageLocators.Row1Cell7_Delete).get_attribute("title") == ElementsPageParameters.TableCell_DeleteTooltip

        assert elementsPage.find_element_wait(
            ElementsPageLocators.Row2Cell1).text.strip() == ElementsPageParameters.R2C1
        assert elementsPage.find_element_wait(
            ElementsPageLocators.Row2Cell2).text.strip() == ElementsPageParameters.R2C2
        assert elementsPage.find_element_wait(
            ElementsPageLocators.Row2Cell3).text.strip() == ElementsPageParameters.R2C3
        assert elementsPage.find_element_wait(
            ElementsPageLocators.Row2Cell4).text.strip() == ElementsPageParameters.R2C4
        assert elementsPage.find_element_wait(
            ElementsPageLocators.Row2Cell5).text.strip() == ElementsPageParameters.R2C5
        assert elementsPage.find_element_wait(
            ElementsPageLocators.Row2Cell6).text.strip() == ElementsPageParameters.R2C6
        assert elementsPage.find_element_wait(ElementsPageLocators.Row2Cell7_Edit).get_attribute(
            "title") == ElementsPageParameters.TableCell_EditTooltip
        assert elementsPage.find_element_wait(ElementsPageLocators.Row2Cell7_Delete).get_attribute(
            "title") == ElementsPageParameters.TableCell_DeleteTooltip

        assert elementsPage.find_element_wait(
            ElementsPageLocators.Row3Cell1).text.strip() == ElementsPageParameters.R3C1
        assert elementsPage.find_element_wait(
            ElementsPageLocators.Row3Cell2).text.strip() == ElementsPageParameters.R3C2
        assert elementsPage.find_element_wait(
            ElementsPageLocators.Row3Cell3).text.strip() == ElementsPageParameters.R3C3
        assert elementsPage.find_element_wait(
            ElementsPageLocators.Row3Cell4).text.strip() == ElementsPageParameters.R3C4
        assert elementsPage.find_element_wait(
            ElementsPageLocators.Row3Cell5).text.strip() == ElementsPageParameters.R3C5
        assert elementsPage.find_element_wait(
            ElementsPageLocators.Row3Cell6).text.strip() == ElementsPageParameters.R3C6
        assert elementsPage.find_element_wait(ElementsPageLocators.Row3Cell7_Edit).get_attribute(
            "title") == ElementsPageParameters.TableCell_EditTooltip
        assert elementsPage.find_element_wait(ElementsPageLocators.Row3Cell7_Delete).get_attribute(
            "title") == ElementsPageParameters.TableCell_DeleteTooltip


        # close application
        actions.UserAction.tearDown_env(driver)


    def test_Elements_Button(self, record_property):
        driver = actions.UserAction.setUp_env(self)
        # click button
        homePage = HomePage(driver)
        CategoryCards = homePage.find_elements_wait(HomePageLocators.CATEGORUCARDS)
        # Click on Elements tab
        CategoryCards[0].click()

        elementsPage = ElementsPage(driver)
        elementsPage.find_element_wait(ElementsPageLocators.Buttons_Menu).click()

        Buttons = elementsPage.find_elements_wait(ElementsPageLocators.Buttons)
        assert (len(Buttons)) == 3

        elementsPage.doubleClick(Buttons[0])
        doubleclickmessage = elementsPage.find_element_wait(ElementsPageLocators.DoubleClickMessage)
        assert doubleclickmessage.text.strip() == ElementsPageParameters.DOUBLECLICKMESSAGE

        elementsPage.rightClick(Buttons[1])
        rightclickmessage = elementsPage.find_element_wait(ElementsPageLocators.RightClickMessage)
        assert rightclickmessage.text.strip() == ElementsPageParameters.RIGHTCLICKMESSAGE

        Buttons[2].click()
        clickmemessage = elementsPage.find_element_wait(ElementsPageLocators.ClickMeMessage)
        assert clickmemessage.text.strip() == ElementsPageParameters.CLICKMEMESSAGE

        # close application
        actions.UserAction.tearDown_env(driver)


    def test_Elements_Link(self, record_property):
        driver = actions.UserAction.setUp_env(self)
        # click button
        actions.UserAction.AccessElementPages(driver)

        elementsPage = ElementsPage(driver)
        elementsPage.find_element_wait(ElementsPageLocators.Links_Menu).click()

        assert elementsPage.find_element(*ElementsPageLocators.Links_Home).is_displayed() == True
        assert elementsPage.find_element(*ElementsPageLocators.Links_HomeFa2mX).is_displayed() == True
        assert elementsPage.find_element(*ElementsPageLocators.Links_Created).is_displayed() == True
        assert elementsPage.find_element(*ElementsPageLocators.Links_NoContent).is_displayed() == True
        assert elementsPage.find_element(*ElementsPageLocators.Links_Moved).is_displayed() == True
        assert elementsPage.find_element(*ElementsPageLocators.Links_BadRequest).is_displayed() == True
        assert elementsPage.find_element(*ElementsPageLocators.Links_Unauthorized).is_displayed() == True
        assert elementsPage.find_element(*ElementsPageLocators.Links_Forbidden).is_displayed() == True
        assert elementsPage.find_element(*ElementsPageLocators.Links_NotFound).is_displayed() == True

        elementsPage.find_element(*ElementsPageLocators.Links_Created).click()
        response = elementsPage.find_element_wait(ElementsPageLocators.Links_Response).text
        assert response.strip() == ElementsPageParameters.LINKCREATED_RESPONSE.strip()

        elementsPage.find_element_wait(ElementsPageLocators.Links_NoContent).click()
        time.sleep(2)
        response = elementsPage.find_element_wait(ElementsPageLocators.Links_Response).text
        assert response.strip() == ElementsPageParameters.LINKNOCONTENT_RESPONSE

        elementsPage.find_element(*ElementsPageLocators.Links_Moved).click()
        time.sleep(2)
        response = elementsPage.find_element_wait(ElementsPageLocators.Links_Response).text
        assert response.strip() == ElementsPageParameters.LINKMOVED_RESPONSE

        elementsPage.find_element(*ElementsPageLocators.Links_BadRequest).click()
        time.sleep(2)
        response = elementsPage.find_element_wait(ElementsPageLocators.Links_Response).text
        assert response.strip() == ElementsPageParameters.LINKBADREQUEST_RESPONSE

        elementsPage.find_element(*ElementsPageLocators.Links_Unauthorized).click()
        time.sleep(2)
        response = elementsPage.find_element_wait(ElementsPageLocators.Links_Response).text
        assert response.strip() == ElementsPageParameters.LINKUNAUTHORIZED_RESPONSE

        elementsPage.find_element(*ElementsPageLocators.Links_Forbidden).click()
        time.sleep(2)
        response = elementsPage.find_element_wait(ElementsPageLocators.Links_Response).text
        assert response.strip() == ElementsPageParameters.LINKFORBIDDEN_RESPONSE

        elementsPage.find_element(*ElementsPageLocators.Links_NotFound).click()
        time.sleep(2)
        response = elementsPage.find_element_wait(ElementsPageLocators.Links_Response).text
        assert response.strip() == ElementsPageParameters.LINKNOTFOUND_RESPONSE


        # close application
        actions.UserAction.tearDown_env(driver)

    def test_BrokenLinks(self, record_property):
        driver = actions.UserAction.setUp_env(self)
        # click button
        actions.UserAction.AccessElementPages(driver)

        elementsPage = ElementsPage(driver)
        elementsPage.find_element_wait(ElementsPageLocators.BrokenLinks_Image_Menu).click()
        BrokenImage = elementsPage.find_element_wait(ElementsPageLocators.BrokenLinks_BrokenImage)
        ValidLink = elementsPage.find_element_wait(ElementsPageLocators.BrokenLinks_ValidLink)
        BrokenLink = elementsPage.find_element_wait(ElementsPageLocators.BrokenLinks_BrokenLink)

        elementsPage.find_element_wait(ElementsPageLocators.BrokenLinks_ValidLink).click()
        assert driver.current_url == UniversialParameters.BASEURL+"/"

        # close application
        actions.UserAction.tearDown_env(driver)


    def test_UploadAndDownload(self, record_property):
        driver = actions.UserAction.setUp_env(self)
        # click button
        actions.UserAction.AccessElementPages(driver)

        elementsPage = ElementsPage(driver)
        elementsPage.find_element_wait(ElementsPageLocators.UploadAndDownload_Menu).click()

        DownloadButton = elementsPage.find_element_wait(ElementsPageLocators.Download_Button)
        DownloadButton.click()
        
        time.sleep(5)
        fileExist = os.path.exists(ElementsPageParameters.SampleFileLocator)
        assert fileExist == True
        os.remove(ElementsPageParameters.SampleFileLocator)

        # Pending on Upload files feature testing, Searching for solution.

        # close application
        actions.UserAction.tearDown_env(driver)


    def test_DynamicProperties(self, record_property):
        driver = actions.UserAction.setUp_env(self)
        # click button
        actions.UserAction.AccessElementPages(driver)

        elementsPage = ElementsPage(driver)
        elementsPage.find_element_wait(ElementsPageLocators.DynamicProperties_Menu).click()
        assert elementsPage.find_element_wait(ElementsPageLocators.Dynamic_WillEnable5Seconds_Button).is_displayed() == True
        time.sleep(5)
        assert elementsPage.find_element_wait(ElementsPageLocators.Dynamic_visibleAfter5Seconds_Buttons).is_displayed() == True

        # close application
        actions.UserAction.tearDown_env(driver)


