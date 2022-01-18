from pageObjects.LoginPage import LoginPage
from selenium import webdriver

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("**Test_001_Login**")
        self.logger.info("**Verifying Home Page**")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Welcome to Athma!":
            assert True
            self.driver.close()
            self.logger.info("**Home page title is passed**")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.info("**Home page title is failed**")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("**Verifying login test**")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Welcome to Athma!":
            assert True
            self.logger.info("**Login test is passed**")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.info("**Login page title is Failed**")
            assert False
