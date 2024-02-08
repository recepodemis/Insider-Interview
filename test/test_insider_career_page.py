import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from constants.global_constant import BASE_URL, CAREERS_LIFE_AT_INSIDER_XPATH, CAREERS_LOCATION_ID, CAREERS_TEAM_ID, CAREERS_XPATH, COMPANY_XPATH

class Test_Insider_Career_Page():
    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self,method):
        self.driver.quit()
    
    def test_career_page(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,COMPANY_XPATH))).click()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,CAREERS_XPATH))).click()
        try: 
            locations = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,CAREERS_LOCATION_ID)))
            assert locations.is_enabled, "Locations not enable at Career page."
            teams = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,CAREERS_TEAM_ID)))
            assert teams.is_enabled, "Teams not exist at Career page."
            life_at_insider = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,CAREERS_LIFE_AT_INSIDER_XPATH)))
            assert life_at_insider.is_enabled, "Life at Insider not exist at Career page."
        except:
            self.driver.save_screenshot("carrer_page_failed_screenshot.png")
        
