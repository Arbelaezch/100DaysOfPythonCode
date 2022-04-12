from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException




url = "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_WT=2&keywords=python%20developer"
chrome_driver_path = "/Users/arbelaezch/code/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

LINKEDIN_PASSWORD = "password"

driver.get(url=url)

button = driver.find_element(by=By.CLASS_NAME, value='cta-modal__primary-btn')
time.sleep(2)
button.click()
time.sleep(2)


username_input = driver.find_element(by=By.ID, value="username")
password_input = driver.find_element(by=By.ID, value="password")

username_input.send_keys("arbelaezch@gmail.com")
password_input.send_keys(LINKEDIN_PASSWORD)

button = driver.find_element(by=By.CLASS_NAME, value="btn__primary--large")
button.click()
time.sleep(3)

wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'jobs-apply-button')))


# easy_apply_btn = driver.find_element(by=By.CLASS_NAME, value='jobs-apply-button')
# button.click()
# time.sleep(2)





# jobs_list = driver.find_elements(By.CLASS_NAME, value='jobs-search-results__list-item occludable-update p0 relative ember-view')
# jobs_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")



my_element_id = 'jobs-apply-button'
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
your_element = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions)\
						.until(EC.presence_of_element_located((By.CLASS_NAME, my_element_id)))
your_element.click()

button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
button.click()
time.sleep(3)


# for job in jobs_list:
# 	try:
# 		job.click()

# 		my_element_id = 'jobs-apply-button'
# 		ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
# 		your_element = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions)\
# 								.until(EC.presence_of_element_located((By.CLASS_NAME, my_element_id)))
# 		your_element.click()
# 		button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
# 		button.click()
# 		time.sleep(3)
# 	except:
# 		print("failed")
    















# print(data.text)

# driver.quit()
