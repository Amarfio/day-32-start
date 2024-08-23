import smtplib
import datetime as dt
import random

my_email = "joshuaamarfio1@gmail.com"
mail_password = "eitckhtbudwcqmwj"


# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=mail_password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="joshuaamarfio1@outlook.com",
#     msg="Subject:Hello\n\nThis is the body of my email."
# )
# connection.close()

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=mail_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="amarfio.joshua@unionsg.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=mail_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )