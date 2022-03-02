# Automatically sends birthday emails to everyone in birthday_info.csv

import smtplib
import datetime as dt
import random
import pandas as pd

my_email = "christian.arbelaez2@gmail.com"
password = "\F*r6MD6be,qFSQ^"

today = dt.datetime.now()
today_tuple = (today.month, today.day)


data = pd.read_csv("Days32-58:Intermediate+/day32/birthday_info.csv")
birthdays_dict = {(data_row["month"], data_row["day"])                  : data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    file_path = f"Days32-58:Intermediate+/day32/letters/letter{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        birthday_person = birthdays_dict[today_tuple]
        contents = letter_file.read()
        contents = contents.replace("[name]", birthday_person["name"])

    # Connect to your email.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
