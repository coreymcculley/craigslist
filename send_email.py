## import required modules
## modules can be imported using pip﻿
import smtplib
from email.mime.text import MIMEText as text

## declare a function that sends email
## this currently works only with gmail but can work with other
## email providers as well with slight modification
## remember to turn on "Access for less secure apps" in GMail via Link beforehand
## https://www.google.com/settings/security/lesssecureapps


def test_sendmail(subject):
##   """ This script contains the parameters required for sending the email """
    to_address ='corey.mcculley@gmail.com'
    body = subject
    subject=subject
    sendmail(to_address, subject, body)

def sendmail(to_address, subject, body): 
    from_address='corey.mcculley@gmail.com' ## change this
    smtp_server = 'smtp.gmail.com'
    smtp_port= 587
    smtp_user="corey.mcculley@gmail.com" ## change this
    smtp_password="" ## change this

    msg = text(body)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()
