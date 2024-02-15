import smtplib

sender_email = 'amanumac@gmail.com'
sender_password = 'ama-news2023'
receiver_email = 'yugoharago@gmail.com'
subject = 'Test email'
body = 'This is a test email sent using Python!'

# Create email message
message = f'Subject: {subject}\n\n{body}'

# Set up SMTP server and login
smtp_server = 'smtp.gmail.com'
port = 587
server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(sender_email, sender_password)

# Send email message
server.sendmail(sender_email, receiver_email, message)

# Quit SMTP server
server.quit()

print('Email sent successfully!')