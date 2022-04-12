from lib2to3.pgen2 import driver
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

		button = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
		button.click()
  
		up_element_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
		
		time.sleep(25)
		self.down = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
  
		time.sleep(25)
		self.up = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')

		print(f"Download: {self.down.text}\nUpload: {self.up.text}")
		



	def tweet_at_provider(self, TWITTER_EMAIL, TWITTER_PASSWORD, PROMISED_DOWN, PROMISED_UP):
		self.driver.get("https://twitter.com/login")

		time.sleep(2)
		email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
		password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

		email.send_keys(TWITTER_EMAIL)
		password.send_keys(TWITTER_PASSWORD)
		time.sleep(2)
		password.send_keys(Keys.ENTER)

		time.sleep(5)
		tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

		tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
		tweet_compose.send_keys(tweet)

		# tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
		# tweet_button.click()
  
		print("success")
		time.sleep(30)
		self.driver.quit()
		
  
  