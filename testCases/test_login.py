#  pytest -rA test_login.py -n=2 --browser edge --html="D:\Automation Notes\Python Project\pythonProject\SVproject\Reports\test_login.html"

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURl = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_HomePageTitle(self, setUp):
        self.logger.info("******** Test_001_Login ********")
        self.logger.info("******** Verify home page Title ********")
        self.driver = setUp
        self.driver.get(self.baseURl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******** Home Page Title test is passed ********")
        else:
            self.driver.save_screenshot("D:\\Automation Notes\\Python Project\\pythonProject\\SVproject\\Screenshots\\test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("******** Home Page Title test is Failed ********")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self, setUp):
        self.logger.info("******** Verify Log in Test ********")
        self.driver = setUp
        self.driver.get(self.baseURl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("******** Log In test is passed ********")
        else:
            self.driver.save_screenshot("D:\\Automation Notes\\Python Project\\pythonProject\\SVproject\\Screenshots\\test_login.png")
            self.driver.close()
            self.logger.error("******** Log In test is failed ********")
            assert False












