import os
import datetime as dt
import pandas
import random
import smtplib

today = (dt.datetime.now().month,dt.datetime.now().day)
MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]

df = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month,data_row.day):data_row for (index,data_row) in df.iterrows()}

if today in birthdays_dict:
    random_letter = random.randint(1,3)
    file_path = f"letter_templates/letter_{random_letter}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        birthday_person = birthdays_dict[today]
        new_contents = contents.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:HAPpy Birthday!!\n\n"
                                f"{new_contents}")
