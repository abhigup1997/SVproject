# pytest -rA test_searchCustomerByEmail.py --html="D:\Automation Notes\Python Project\pythonProject\SVproject\Reports\test_searchCustomerByEmail.html"

import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import Addcustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURl = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchCustomerByEmail(self, setUp):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver = setUp
        self.driver.implicitly_wait(120)
        self.driver.get(self.baseURl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = Addcustomer(self.driver)

        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by emailID **********")

        self.searchcust = SearchCustomer(self.driver)

        self.searchcust.setEmail("victoria_victoria@nopCommerce.com")

        time.sleep(5)

        self.searchcust.clickSearch()

        time.sleep(5)

        status = self.searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")

        if True == status :
            assert True
            self.logger.info("************* search customer found **********")
        else:
            self.logger.info("************* search customer not found **********")
            self.driver.save_screenshot("D:\\Automation Notes\\Python Project\\pythonProject\\SVproject\\Screenshots\\test_searchCustomerByEmail.png")
            assert False

        self.driver.close()
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
