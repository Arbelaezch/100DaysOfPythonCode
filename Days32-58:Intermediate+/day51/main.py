from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from InternetSpeedTwitterBot import InternetSpeedTwitterBot


PROMISED_DOWN = 100
PROMISED_UP = 50
CHROME_DRIVER_PATH = "/Users/arbelaezch/code/chromedriver"
TWITTER_EMAIL = "arbelaezch@gmail.com"
TWITTER_PASSWORD = "Sherlocked#1"

url = "http://secure-retreat-92358.herokuapp.com/"

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

speed = bot.get_internet_speed()
# bot.tweet_at_provider()


# data = driver.find_element(by=By.NAME, value='fName')
# data.send_keys("Carb")



# print(data.text)

# driver.quit()

