import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from constants.global_constant import *

class Test_Insider_Qa_Filter():
    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(QA_URL)
        self.driver.maximize_window()

    def teardown_method(self,method):
        self.driver.quit()
    
    def test_QA_filter(self):
        try:
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,SEE_ALL_QA_JOBS_BUTTON_XPATH))).click()
            WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element((By.XPATH,DEPARTMENT_CONTAINER_XPATH),"Quality Assurance"))
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,LOCATIONS_FILTER_XPATH))).click()
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,ISTANBUL_LOCATION_XPATH))).click()
            time.sleep(3)
            jobs = self.driver.find_elements(By.CLASS_NAME,POSITION_LIST_ITEM_CLASSNAME)
            assert len(jobs) == 3
        except:
            self.driver.save_screenshot("QA_filter_failed_screenshot.png")

    def test_QA_filter_result(self):
        try:
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,SEE_ALL_QA_JOBS_BUTTON_XPATH))).click()
            WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element((By.XPATH,DEPARTMENT_CONTAINER_XPATH),"Quality Assurance"))
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,LOCATIONS_FILTER_XPATH))).click()
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,ISTANBUL_LOCATION_XPATH))).click()
            time.sleep(3)
            department_position = self.driver.find_elements(By.CLASS_NAME,DEPARTMENT_POSITION_CLASSNAME)
            location_positions = self.driver.find_elements(By.CLASS_NAME,LOCATION_POSITION_CLASSNAME)
            assert department_position.text == "Quality Assurance"
            assert location_positions.text == "Istanbul, Turkey"
        except:
            self.driver.save_screenshot("QA_filter_result_failed_screenshot.png")

    def test_view_role(self):
        try:
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,SEE_ALL_QA_JOBS_BUTTON_XPATH))).click()
            WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element((By.XPATH,DEPARTMENT_CONTAINER_XPATH),"Quality Assurance"))
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,LOCATIONS_FILTER_XPATH))).click()
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,ISTANBUL_LOCATION_XPATH))).click()
            time.sleep(3)
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,VIEW_ROLE_BUTTON_XPATH))).click()
            WebDriverWait(self.driver,5).until(EC.url_contains(LEVER_APP_URL))
            assert LEVER_APP_URL == self.driver.current_url
        except:
            self.driver.save_screenshot("view_role_button_failed_screenshot.png")
