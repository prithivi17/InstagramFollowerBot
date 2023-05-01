import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "D:\Python course\chromedriver_win32\chromedriver.exe"
INSTA_USERNAME = os.environ.get('INSTA_USERNAME')
INSTA_PASSWORD = os.environ.get('INSTA_PASSWORD')
SIMILAR_ACCOUNT = "gaming"

class InstaFollower:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(executable_path=CHROME_DRIVER_PATH))

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(INSTA_USERNAME)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(INSTA_PASSWORD)
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login.click()

    def find_followers(self):
        time.sleep(4)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(5)

    def follow(self):
        try:
            list_of_followers = self.driver.find_elements(By.XPATH, "//button[contains(.,'Follow')]")
            for btn in list_of_followers:
                self.driver.execute_script("arguments[0].click();", btn)
                time.sleep(2)

        except Exception as e:
            print(e)



