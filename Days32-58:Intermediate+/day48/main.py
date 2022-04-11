from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = "https://www.python.org/"
chrome_driver_path = "/Users/arbelaezch/code/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url=url)

# price = (str((driver.find_element_by_class_name(name="a-offscreen").text)).split("$"))[1]

# price = driver.find_element(by=By.CLASS_NAME , value="a-offscreen")

# price = driver.find_element(by="CLASS_NAME", value="a-offscreen")
# price = driver.find_element(By.XPATH, value='//*[@id="corePrice_feature_div"]/div/span/span[1]')

# price = driver.find_element_by_css_selector(css_selector="span.a-offscreen")
# print(price.text)

# title = driver.find_element_by_id("productTitle")
# title = driver.find_element_by_css_selector("span.product-title-word-break")
# title = driver.find_element(by=By.CLASS_NAME, value='a-offscreen')
# print(title.text)



data = driver.find_elements(by=By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')

data_dict = {}

num = 0

for event in data:
    n = event.text.split("\n")
    data_dict[num] = {}
    data_dict[num]["time"] = n[0]
    data_dict[num]["name"] = n[1]

    num += 1
    
print(data_dict)
    


# Input forms
# Can access size, tag, placeholder, etc
# search_bar = driver.find_element_by_name("search")
# print(search_bar.get_attribute("placeholder"))
# search_bar.send_keys("Python ")
# search_bar.send_keys(Keys.ENTER)


# Useful for finding links you want to interact with.
# driver.find_element_by_link_text("Link Text")












# Closes the open page
# driver.close()
# Quits the entire browser
driver.quit()

