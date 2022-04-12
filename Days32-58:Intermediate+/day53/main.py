from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import requests
from bs4 import BeautifulSoup


listings_url = "https://www.zillow.com/st-albert-ab/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22St.%20Albert%2C%20AB%22%2C%22mapBounds%22%3A%7B%22west%22%3A-113.82609097750215%2C%22east%22%3A-113.35230557711152%2C%22south%22%3A53.46808993769371%2C%22north%22%3A53.7345647819556%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A791606%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A476824%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
survey_url = "https://docs.google.com/forms/d/e/1FAIpQLSfOGDIhE5Zvqomgo7Z4_0Pq4QmMUDHuTnU5FZAUXXbAHT1DWw/viewform?usp=sf_link"
chrome_driver_path = "/Users/arbelaezch/code/chromedriver"

r = requests.get(listings_url, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36", "Accept-Language": "en-US,en;q=0.9"})
listings_web_page = r.text


soup = BeautifulSoup(listings_web_page, "html.parser")

address_list = []
price_list = []
link_list = []

# FINDS PRICE
for link in soup.find_all("div", class_= "list-card-price"):
    # print(link.text)
    price_list.append(link.text)
	

for link in soup.find_all("div", class_= "list-card-info"):  
    # FINDS ADDRESS
	address_list.append(link.text.split("C$")[0])
	# print(link.text.split("C$")[0])
    
	try:
		# FINDS LINK
		addr = str(link.find("a")).split('href="')[1]
		addr = addr.split('"')[0]
		link_list.append(addr)
		# print(addr)
	except:
		pass

num = 0
if len(address_list) != 0:
	# Selenium fills in google form.
	driver = webdriver.Chrome(executable_path=chrome_driver_path) 
	driver.get(url=survey_url)
    
	while num < len(address_list):
		time.sleep(3)

		input1 = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
		input2 = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
		input3 = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
		input1.send_keys(address_list[num])
		input2.send_keys(price_list[num])
		input3.send_keys(link_list[num])

		driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()

		time.sleep(3)

		driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
		num += 1


# print(data.text)

# driver.quit()
    
    
# print(address_list)
# print(price_list)
# print(link_list)
    
    

    
    
    


# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# price = (str((soup.find(name="span", class_="a-offscreen").text)).split("$"))[1]

# driver.get(url=survey_url)

# data = driver.find_element(by=By.NAME, value='fName')
# data.send_keys("Carb")

# print(data.text)

# driver.quit()