import smtplib
from email.mime.text import MIMEText

with open("email.txt") as fp:
    msg = MIMEText(fp.read())

from_email = "Serban Bkebea <mihaiserban.blebea@gmail.com>"
to_email = "serban_pt@me.com"

msg['Subject'] = "Helo"
msg['From'] = from_email
msg['To'] = to_email

host = "smtp.gmail.com"
port = 465

gmail_user = "mihaiserban.blebea@gmail.com"
gmail_password = "highprotein07"

try:
   server = smtplib.SMTP_SSL(host, port)
   server.login(gmail_user, gmail_password)
   server.sendmail(from_email, to_email, msg.as_string())
   server.close()
except smtplib.SMTPException:
   print ("Error: unable to send email")