import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email = "christian.arbelaez2@gmail.com"
password = "\F*r6MD6be,qFSQ^"

book_url = "https://www.amazon.ca/gp/product/0132350882/ref=ox_sc_saved_title_6?smid=A3DWYIK6Y9EEQB&psc=1"

HISTORICAL_LOW = 40

r=requests.get(book_url, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36", "Accept-Language": "en-US,en;q=0.9"})
amazon_web_page = r.text

soup = BeautifulSoup(amazon_web_page, "lxml")

price = (str((soup.find(name="span", class_="a-offscreen").text)).split("$"))[1]

if price <= HISTORICAL_LOW:
    contents = f"This product is at or below a historical low price. {book_url}"
    # Connect to your email.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs="arbelaezch@gmail.com",
            msg=f"Subject:Amazon Historical Low\n\n{contents}"
        )


