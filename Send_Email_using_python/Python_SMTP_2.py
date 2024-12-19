import smtplib
import logging
recipient_email=['vinaypate94@gmail.com',"vp023405@gmail.com"]
for i in recipient_email:
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "vp023405@gmail.com"
    app_password = "tyeo yyke dsgo cplj"  
    email_body = "Subject: Test Email\n\nThis is a test email with proper authentication."

try:
    # Connect to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to secure
    server.login(sender_email, app_password)  # Authenticate
    server.sendmail(sender_email, recipient_email, email_body)  # Send email
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError as auth_error:
    print("Authentication error:", auth_error)
except Exception as e:
    print("An error occurred:", e)
finally:
    server.quit()  # Ensure the connection is closed