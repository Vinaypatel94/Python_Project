import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
import logging

logger = logging.getLogger(__name__)

env = Environment(loader=FileSystemLoader('send_mail_using_jinaja2/template')) 
template = env.get_template('Email_template.txt')

context={

    "title":"jinja2 SMTP Email testing",
    "name":"vinay Patel",
}
#render the mail
email_body = template.render(context)
with open("email_output.txt",'w') as file:
    file.write(email_body)

recipient_emails=['vinaypate94@gmail.com','vp023405@gmail.com']

#server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "vp023405@gmail.com"
app_password = "tyeo yyke dsgo cplj" 
#setup Emial
sender_email = "vp023405@gmail.com"
recipient_email = "vinaypate94@gmail.com"
subject="jinja 2 testng"

for i in recipient_emails:
    # Create email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] =  ','.join(recipient_emails)
    msg["Subject"] = subject
    msg.attach(MIMEText(email_body,"html"))

# print("email_body", email_body)
# print("msg.as_string", msg.as_string())

try:
    # Connect to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to secure
    server.login(sender_email, app_password)  # Authenticate
    server.sendmail(sender_email, recipient_emails, msg.as_string())  # Send email
    print("Email sent successfully!")

except smtplib.SMTPAuthenticationError as auth_error:
    print("Authentication error:", auth_error)
except Exception as e:
    print("An error occurred:", e)
    logger.error("Getting error", exc_info=True)
finally:
    server.quit()  



