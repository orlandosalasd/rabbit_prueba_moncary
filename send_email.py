# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(message):
    # create message object instance
    msg = MIMEMultipart()

    message = message

    # setup the parameters of the message
    password = "osd1143382275"
    msg['From'] = "osalas@lsv-tech.com"
    msg['To'] = "orlandosalasdiaz@hotmail.com"
    msg['Subject'] = "Prueba"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.lsv-tech.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    return print("successfully sent email to %s:" % (msg['To']))