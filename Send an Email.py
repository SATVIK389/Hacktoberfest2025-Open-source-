import smtplib

sender = "your_email@gmail.com"
password = "your_password"
receiver = "receiver_email@gmail.com"
message = "Subject: Hello from Python\n\nThis is a test email."

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
print("Email sent successfully!")
