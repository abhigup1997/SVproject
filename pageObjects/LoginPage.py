# NopCommerce.com
# nehop82885@fsouda.com
# Password@1234
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_Email_id = "Email"
    textbox_Password_id = "Password"
    button_login_xpath = "//button"
    button_logout_linkText = "Logout"


    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.textbox_Email_id).clear()
        self.driver.find_element(By.ID, self.textbox_Email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_Password_id).clear()
        self.driver.find_element(By.ID, self.textbox_Password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.button_logout_linkText).click()


