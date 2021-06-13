from selenium.webdriver.common.by import By
import re

class LeftPanelLocators():
    BookStoreApp_MenuItem = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[6]/span/div/div[1]/text()')
    BookStoreApp_Login = (By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div/div/div[6]/div/ul/li[1]/span')
    BookStoreApp_BookStore = (By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div/div/div[6]/div/ul/li[2]/span')
    BookStoreApp_Profile = (By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div/div/div[6]/div/ul/li[3]/span')
    BookStoreApp_BookStoreAPI = (By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div/div/div[6]/div/ul/li[4]/span')

class HomePageLocators():
    ELEMENTS_LINK = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[3]/h5')
    FORMS_LINK = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[3]/h5')
    ALERTS_FRAME_WIDNOWS_LINK = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[3]/h5')
    WIDGETS_LINK = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[4]/div/div[3]/h5')
    INTERACTIONS_LINK = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[5]/div/div[3]/h5')
    BOOKSTOREAPPLICATION_LINK = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[6]/div/div[3]/h5')
    CATEGORUCARDS = (By.XPATH, '//*[@id="app"]//div[@class="card mt-4 top-card"]')

class BookStoreApplicationPageLocators():
    Login_button = (By.ID, 'login')
    SearchBox_Input = (By.ID, 'searchBox')
    TableHeader_1 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div[1]')
    TableHeader_2 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[1]')
    TableHeader_3 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[3]/div[1]')
    TableHeader_4 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[4]/div[1]')
    BookName_1 = (By.XPATH, '//*[@id="see-book-Git Pocket Guide"]')
    SIGNIN_USERNAME = (By.XPATH, '//*[@id="userName-value"]')

class LoginPageLocators():
    UserName_Input = (By.XPATH, '//*[@id="userName"]')
    Password_Input = (By.XPATH, '//*[@id="password"]')
    Login_button = (By.XPATH, '//*[@id="login"]')
    NewUser_Input = (By.XPATH, '//*[@id="newUser"]')

class ElementsPageLocators():
    Elements_Menu = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[1]/span')
    TextBox_Menu = (By.XPATH, '//*[@id="item-0"]/span')
    CheckBox_Menu = (By.XPATH, '//*[@id="item-1"]/span')
    RadioButton_Menu = (By.XPATH, '//*[@id="item-2"]/span')
    WebTables_Menu = (By.XPATH, '//*[@id="item-3"]/span')
    Buttons_Menu = (By.XPATH, '//*[@id="item-4"]/span')
    Links_Menu = (By.XPATH, '//*[@id="item-5"]/span')
    BrokenLinks_Image_Menu = (By.XPATH, '//*[@id="item-6"]')
    UploadAndDownload_Menu = (By.XPATH, '//*[@id="item-7"]/span')
    DynamicProperties_Menu = (By.XPATH, '//*[@id="item-8"]/span')

    TextBox_FullName_Input = (By.XPATH, '//*[@id="userName"]')
    TextBox_Email_Input = (By.XPATH, '//*[@id="userEmail"]')
    TextBox_CurrentAddress_Input = (By.XPATH, '//*[@id="currentAddress"]')
    TextBox_PermanentAddress_Input = (By.XPATH, '//*[@id="permanentAddress"]')
    TextBox_Submit_Button = (By.XPATH, '//*[@id="submit"]')

    TextBox_Name = (By.XPATH, '//*[@id="name"]')
    TextBox_Email = (By.XPATH, '//*[@id="email"]')
    TextBox_CurrentAddress = (By.ID, 'currentAddress')
    TextBox_PermanentAddress = (By.XPATH, '//*[@id="permanentAddress"]')
    TextBox_Outputs = (By.XPATH, '//*[@id="output"]/div/p[@class="mb-1"]')

    Home_checkBox = (By.XPATH, '//*[@class="rct-checkbox"]')
    Home_checkBox_values = (By.XPATH, '//*[@id="result"]/span')
    Home_checkBox_icon = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/button/svg')

    Yes_RadioButton = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[2]/label[@for="yesRadio"]')
    Impressive_RadioButton = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/label[@for="impressiveRadio"]')
    No_RadioButton = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[4]/label[@for="noRadio"]')
    RadioButton_Selected = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/p[@class="mt-3"]')

    TableHeaders = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[@role="columnheader"]')
    FirstHeader = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[1]')
    SecondHeader = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[2]/div[1]')
    ThirdHeader = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[3]/div[1]')
    FourthHeader = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[4]/div[1]')
    FifthHeader = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[5]/div[1]')
    SixthHeader = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[6]/div[1]')
    SeventhHeader = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[7]/div[1]')

    Row1Cell1 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]')
    Row1Cell2 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[2]')
    Row1Cell3 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[3]')
    Row1Cell4 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[4]')
    Row1Cell5 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[5]')
    Row1Cell6 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[6]')
    Row1Cell7_Edit = (By.XPATH, '//*[@id="edit-record-1"]')
    Row1Cell7_Delete = (By.XPATH, '//*[@id="delete-record-1"]')

    Row2Cell1 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div/div[1]')
    Row2Cell2 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div/div[2]')
    Row2Cell3 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div/div[3]')
    Row2Cell4 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div/div[4]')
    Row2Cell5 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div/div[5]')
    Row2Cell6 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div/div[6]')
    Row2Cell7_Edit = (By.XPATH, '//*[@id="edit-record-2"]')
    Row2Cell7_Delete = (By.XPATH, '//*[@id="delete-record-2"]')

    Row3Cell1 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div/div[1]')
    Row3Cell2 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div/div[2]')
    Row3Cell3 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div/div[3]')
    Row3Cell4 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div/div[4]')
    Row3Cell5 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div/div[5]')
    Row3Cell6 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div/div[6]')
    Row3Cell7_Edit = (By.XPATH, '//*[@id="edit-record-3"]')
    Row3Cell7_Delete = (By.XPATH, '//*[@id="delete-record-3"]')

    Button_DoubleClick = (By.XPATH, '//*[@id="doubleClickBtn"]')
    Button_RightClickMe = (By.XPATH, '//*[@id="rightClickBtn"]')
    Button_ClickMe = (By.XPATH, '//*[@id="rsrJx"]')
    DoubleClickMessage = (By.XPATH, '//*[@id="doubleClickMessage"]')
    RightClickMessage = (By.XPATH, '//*[@id="rightClickMessage"]')
    ClickMeMessage = (By.XPATH, '//*[@id="dynamicClickMessage"]')
    Buttons = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/button')

    Links_Home = (By.XPATH, '//*[@id="simpleLink"]')
    Links_HomeFa2mX = (By.XPATH, '//*[@id="dynamicLink"]')
    Links_Created = (By.XPATH, '//*[@id="created"]')
    Links_NoContent = (By.XPATH, '//*[@id="no-content"]')
    Links_Moved = (By.XPATH, '//*[@id="moved"]')
    Links_BadRequest = (By.XPATH, '//*[@id="bad-request"]')
    Links_Unauthorized = (By.XPATH, '//*[@id="unauthorized"]')
    Links_Forbidden = (By.XPATH, '//*[@id="forbidden"]')
    Links_NotFound = (By.XPATH, '//*[@id="invalid-url"]')
    Links_Response = (By.XPATH, '//*[@id="linkResponse"]')


    BrokenLinks_BrokenImage = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/img[2]')
    BrokenLinks_ValidLink = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/a[1]')
    BrokenLinks_BrokenLink = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/a[2]')

    Download_Button = (By.XPATH, '//*[@id="downloadButton"]')
    ChooseFile_Button = (By.XPATH, '//*[@id="uploadFile"]')\

    Dynamic_WillEnable5Seconds_Button = (By.XPATH, '//*[@id="enableAfter"]')
    Dynamic_ColorChange_Button = (By.XPATH, '//*[@id="colorChange"]')
    Dynamic_visibleAfter5Seconds_Buttons = (By.XPATH, '//*[@id="visibleAfter"]')

class FormsPageLocators():
    PracticeForm_Link = (By.XPATH, '//*[@id="item-0"]/span')
    FirstName_field = (By.XPATH, '//*[@id="firstName"]')
    LastName_field = (By.XPATH, '//*[@id="lastName"]')
    Email_field = (By.XPATH, '//*[@id="userEmail"]')
    Mail_option = (By.XPATH, )









