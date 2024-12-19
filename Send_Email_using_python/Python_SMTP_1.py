import smtplib
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("vp023405@gmail.com","tyeo yyke dsgo cplj")
email_body='subject:Testing mail\n\nTest email with corrent Authentication'
server.sendmail('vp023405@gmail.com','vinaypate94@gmail.com',email_body)
print('email sent')
