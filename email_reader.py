from imbox import Imbox
from datetime import datetime
import pandas as pd

username = "gabgui2001@outlook.com"
password = open("pass", 'r').read()
host = "imap-mail.outlook.com"

mail = Imbox(host, username=username, password=password, ssl=True)
messages = mail.messages()


for (uid, message) in messages:
    message.body.html
    break