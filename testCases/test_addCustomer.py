# pytest -rA test_addCustomer.py --html="D:\Automation Notes\Python Project\pythonProject\SVproject\Reports\test_addCustomer.html"


import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import Addcustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_AddCustomer:
    baseURl = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_addCustomer(self, setUp):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setUp
        self.driver.get(self.baseURl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = Addcustomer(self.driver)

        self.addcust.clickOnCustomersMenu()
        time.sleep(3)
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(3)
        self.addcust.clickOnAddnew()
        time.sleep(3)

        self.logger.info("************* Providing customer info **********")

        self.ran_email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.ran_email)
        time.sleep(2)
        self.addcust.setPassword("test123")
        time.sleep(2)
        self.addcust.setFirstName("Shubham")
        time.sleep(2)
        self.addcust.setLastName("Shinde")
        time.sleep(2)
        self.addcust.setGender("Male")
        time.sleep(2)
        self.addcust.setDob("07/09/1998")
        time.sleep(2)
        self.addcust.setCompanyName("busyQA")
        time.sleep(2)
        self.addcust.setCustomerRoles("Guests")
        time.sleep(2)
        self.addcust.setManagerOfVendor("Vendor 2")
        time.sleep(2)
        self.addcust.setAdminContent("This is for testing.........")
        time.sleep(2)
        self.addcust.clickOnSave()
        time.sleep(4)

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot("D:\\Automation Notes\\Python Project\\pythonProject\\SVproject\\Screenshots\\test_addCustomer.png")
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")



def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))