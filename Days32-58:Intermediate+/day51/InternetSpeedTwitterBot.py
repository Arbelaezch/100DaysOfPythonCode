from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException



class InternetSpeedTwitterBot():
    
	def __init__(self, driver_path) -> None:	
		self.driver = webdriver.Chrome(executable_path=driver_path)
		self.up = 0
		self.down = 0


	def get_internet_speed(self):
		url = 'https://www.speedtest.net/'
		self.driver.get(url=url)

		button = self.driver.find_element(by=By.CLASS_NAME, value='js-start-test test-mode-multi')
		button.click()
  
		up_element_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
		ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
		your_element = WebDriverWait(self.driver, 10,ignored_exceptions=ignored_exceptions)\
						.until(EC.presence_of_element_located((By.CLASS_NAME, up_element_xpath)))
      
		print(your_element.text)
		
  
		# data = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
  


	def tweet_at_provider(self):
		pass
		
  
  