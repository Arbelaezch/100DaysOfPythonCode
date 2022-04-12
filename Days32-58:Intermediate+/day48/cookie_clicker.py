from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



url = "https://orteil.dashnet.org/cookieclicker/"
chrome_driver_path = "/Users/arbelaezch/code/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

xpath = '//*[@id="bigCookie"]'

driver.get(url=url)


timeout = time.time() + 5
five_min = time.time() + 60*5


num = -1
while 1:
	try:
		cookie = driver.find_element(by=By.XPATH, value=xpath)
		cookie.click()
	except:
		pass
 
	# if time.time() > timeout:
	# 	try:
	# 		upgrade = driver.find_elements(by=By.CLASS_NAME, value='price')
	# 		cookies = driver.find_element(by=By.ID, value="cookies").text
   
	# 		upgrade2 = [item.text for item in upgrade]
   
	# 		upgrade2 = list(filter(None, upgrade2))

	# 		while upgrade2[num] > cookies:
	# 			num -= 1

			
	# 		for n in range(0, len(upgrade)):
	# 			if upgrade[n] == upgrade2[num]:
	# 				upgrade[n].click()
	# 			else:
	# 				pass

	# 		num = -1
	# 		timeout = time.time() + 5
	# 	except:
	# 		driver.quit()


