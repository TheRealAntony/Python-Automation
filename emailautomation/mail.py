#!/usr/bin/python3
# author: jithuantony4u@gmail.com
# description: this python script will help to send email

import yagmail
import os

sender = 'ownermail@gmail.com'
receiver = 'receivermail@test.com'

subject = "This is the subject!"


contents = """
Here is the content of the email! 
Hi!
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")