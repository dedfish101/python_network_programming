import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "dedfish404@outlook.com"
TO_EMAIL = "nomala5378@inpsur.com" # which email to send
PASSWORD = getpass.getpass("Enter password: ") #takes pass from user 

message = MIMEMultipart("alternative")
message['Subject'] = "test"
message['From'] = FROM_EMAIL
message['To'] = TO_EMAIL
message['Cc'] = FROM_EMAIL
message['Bcc'] = FROM_EMAIL #iinit

html = ""
with open("mail.html", "r") as file:
    html = file.read()#from where to take the mail content 

html_part = MIMEText(html, 'html')
message.attach(html_part)

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())#sending mail 
smtp.quit()