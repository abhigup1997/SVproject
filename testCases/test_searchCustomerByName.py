# pytest -rA test_searchCustomerByName.py --html="D:\Automation Notes\Python Project\pythonProject\SVproject\Reports\test_searchCustomerByName.html"

import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import Addcustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseURl = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchCustomerByEmail(self, setUp):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver = setUp
        self.driver.implicitly_wait(120)
        self.driver.get(self.baseURl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = Addcustomer(self.driver)

        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by name **********")

        self.searchcust = SearchCustomer(self.driver)

        self.searchcust.setFirstName("Victoria")

        self.searchcust.setLastName("Terces")

        self.searchcust.clickSearch()

        time.sleep(3)

        status = self.searchcust.searchCustomerByName("Victoria Terces")

        if True == status :
            assert True
            self.logger.info("************* search customer found **********")
        else:
            self.logger.info("************* search customer not found **********")
            self.driver.save_screenshot("D:\\Automation Notes\\Python Project\\pythonProject\\SVproject\\Screenshots\\test_searchCustomerByName.png")
            assert False

        self.driver.close()
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")
