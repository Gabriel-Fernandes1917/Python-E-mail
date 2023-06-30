from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes
#server SMTP

email_senha = open('pass', 'r').read()

email_origem = ''
email_destino = ('')

assunto = "Ola so um test"

body = open('menssagem.txt', 'r').read()


# class for create one e-mail
menssagem = EmailMessage()

menssagem["From"] = email_origem
menssagem["To"] = email_destino
menssagem["Subject"] = assunto


menssagem.set_content(body)

# ssl crypt
safe = ssl.create_default_context()

#with open and close one connection, the pythom
#with outher service
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(email_origem, email_senha)
    smtp.sendmail(email_origem,email_destino, menssagem.as_string())