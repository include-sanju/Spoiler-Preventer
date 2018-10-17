#Function to send email using the following modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import env

def send_email(subject,mail_content,emailto):
    try:
        server = smtplib.SMTP('smtp.gmail.com' , 587)
        server.ehlo()
        server.starttls()
        #taking email and password from updates strings in env.py
        server.login(env.EMAIL, env.EMAIL_PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject,mail_content)
        server.sendmail(env.EMAIL, emailto, message)
        server.quit()
    except:
        pass
        #if any error occurs
        print('FAILED!')