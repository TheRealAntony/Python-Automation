import smtplib
import os

sender = 'antony.test@gmail.com'
receiver = 'test2@gmail.com'
password = 'python12345678'

message = """\
Subject: Hello Hello

This is Ardit!
Just wanted to say hi!
"""

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()