import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # For TLS
sender_email = 'mailbot304@gmail.com'
sender_password = 'Mail123@BOT'
receiver_email = 'boiknow215@gmail.com'
subject = 'Automated Email'
message = 'This is an automated email sent using Python.'

# Create a MIME message
msg = MIMEMultipart()
msg['From'] = 'mailbot304@gmail.com'
msg['To'] = 'boiknow215@gmail.com'
msg['Subject'] = 'Automated_Email'

# Attach the message
msg.attach(MIMEText(message, 'plain'))

# Create a server instance
server = smtplib.SMTP(smtp_server, smtp_port)

# Start TLS encryption
server.starttls()

# Login to your Gmail account
server.login(sender_email, sender_password)

# Send the email
server.sendmail(sender_email, receiver_email, msg.as_string())

# Quit the server
server.quit()

print('Email sent successfully!')