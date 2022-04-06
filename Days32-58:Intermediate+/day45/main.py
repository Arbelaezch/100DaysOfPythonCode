from urllib import response
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.bfi.org.uk/sight-and-sound/greatest-films-all-time")
sNs_web_page = response.text

soup = BeautifulSoup(sNs_web_page, "html.parser")

all_movies = soup.select("h2 a")

 
num = 1
 
with open("Days32-58:Intermediate+/day45/movies.txt", "w") as file:
	for movie in all_movies:
		print()
		file.write(f"{str(num)}. {movie.getText()}")
		file.write('\n')
		num += 1
