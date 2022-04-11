from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



url = "http://secure-retreat-92358.herokuapp.com/"
chrome_driver_path = "/Users/arbelaezch/code/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url=url)

data = driver.find_element(by=By.NAME, value='fName')
data.send_keys("Carb")

# print(data.text)

# driver.quit()