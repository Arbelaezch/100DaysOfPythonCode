from bs4 import BeautifulSoup

with open("Days32-58:Intermediate+/day45/website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")

anchor_tags = soup.find_all("a")
heading = soup.find(name="h1", id="name")
section_heading = soup.find(name="h3", class_="heading")
class_is_heading = soup.find_all(class_="heading")
h3_heading = soup.find_all("h3", class_="heading")
company_url = soup.select_one(selector="p a")

all_anchor_tags = soup.find_all(name="a")
print(heading.getText())
print(company_url.get("href"))

    
# print(soup.title)