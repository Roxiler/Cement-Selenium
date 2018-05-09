from selenium.webdriver.common.by import By

import time

class Login:

    def __init__(self, browser, config, data):
        
        # Assigning class level variables
        self.browser = browser
        self.config = config
        self.dataset = data

        # Locating and assigning elements from the page
        # To class level varaibles for further usage
        self.french = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/form/div[6]/div[2]')
        self.english = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/form/div[6]/div[1]')
        self.submit = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/form/div[4]/div/button')
        self.username = browser.find_element_by_name("username")
        self.password = browser.find_element_by_name("password")

    def change_language(self):

        # Changes language to test globalization
        if self.dataset.get('language') == "fr":
            self.french.click()
            self.french.click()

        if self.dataset.get('language') == "en":            
            self.english.click()
            self.english.click()

    def run(self):

        self.change_language()
        self.username.send_keys(self.dataset.get('username'))
        self.password.send_keys(self.dataset.get('password'))
        self.submit.click()
