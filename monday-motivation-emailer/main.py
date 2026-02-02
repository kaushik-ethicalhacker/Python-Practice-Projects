import smtplib as smtp
import datetime as dt
import random as rd


password = ""
sender_email = ""
receiver_email = ""

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt", "r") as quote:
        quotes = quote.readlines()
        quotee = rd.choice(quotes)

    with smtp.SMTP("smtp.gmail.com") as smtp:
        smtp.starttls()
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, receiver_email, f"Subject: Monday Motivation\n\n{quotee}")

