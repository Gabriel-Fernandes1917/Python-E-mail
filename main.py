from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes
#server SMTP

email_senha = open('pass', 'r').read()

email_origem = 'gabgui2001@outlook.com'
email_destino = ('gabgui2001@gmail.com')

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
with smtplib.SMTP('smtp.office365.com', port=587) as smtp:
    smtp.starttls(context=safe)
    smtp.login(email_origem, "akjonfoymnnhniny")
    smtp.sendmail(email_origem,email_destino, menssagem.as_string())