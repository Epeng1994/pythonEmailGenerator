import os
import ssl
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()
#import from python

#declare email variables
email_sender = 'cursedkittenz@gmail.com'
email_password = os.getenv('password')

email_receiver = 'nedom70199@chnlog.com'
subject = 'Test2'
body = """
Test2
"""

em  = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())