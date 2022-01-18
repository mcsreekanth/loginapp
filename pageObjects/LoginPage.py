class LoginPage:
    # Login Page
    textbox_username_id_xpath = "//input[@id='username']"
    textbox_password_id_xpath = "//input[@id='password']"
    button_login_xpath = "//button[@type='submit']"
    button_logout_xpath = "//span[text()='Sign out']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username: object) -> object:
        self.driver.find_element_by_xpath(self.textbox_username_id_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_username_id_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_id_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_id_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()
