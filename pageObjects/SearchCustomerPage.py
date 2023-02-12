from selenium.webdriver.common.by import By


class SearchCustomer:
    #  Search Customer Page
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tblSearchResults_xpath = '//*[@id="customers-grid"]/tbody'
    tableRows_xpath = '//*[@id="customers-grid"]/tbody/tr'
    tableColumns_xpath = '//*[@id="customers-grid"]/tbody/tr[1]/td'

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lastname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEmail(self, Email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            email = self.driver.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr['+str(r)+']/td[2]').text
            if email == Email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            name = self.driver.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr[' + str(r) + ']/td[3]').text
            if name == Name:
                flag = True
                break
        return flag
