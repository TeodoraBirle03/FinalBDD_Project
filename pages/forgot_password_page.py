from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Forgot_password_page(Browser):
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Enter your email"]')
    SEND_EMAIL_BTN = (By.XPATH, '//span[text() = "Send email"]/parent::button')


    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def click_send_email_btn(self):
        self.driver.find_element(*self.SEND_EMAIL_BTN).click()