import datetime as dt
import pandas as pd
import random as rnd
import smtplib as smtp

my_email = ""
password = ""
receiver_email = ""

today = dt.date.today()
today_tuple = (today.month, today.day)

df = pd.read_csv("birthdays.csv")

birthday_dict = {(df_row["month"],df_row["day"]): df_row for (index,df_row) in df.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file = f"letter_{rnd.randint(1,3)}.txt"
    with open(file) as f:
        content = f.read()
        content = content.replace("[Name]", birthday_person["name"])

    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=receiver_email,msg=f"Subject: Happy Birthday! \n\n{content}")





