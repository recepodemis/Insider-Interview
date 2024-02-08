import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from constants.global_constant import *

class Test_Insider():
    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self,method):
        self.driver.quit()
    
    def test_homepage(self):
        try:
            insider_logo = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,INSIDER_LOGO_XPATH)))
            assert insider_logo.is_enabled
        except:
            self.driver.save_screenshot("homepage_failed_screenshot.png")
    

