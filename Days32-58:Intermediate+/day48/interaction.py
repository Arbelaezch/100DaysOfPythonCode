from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://en.wikipedia.org/wiki/Main_Page"
chrome_driver_path = "/Users/arbelaezch/code/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url=url)

data = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')

print(data.text)

driver.quit()