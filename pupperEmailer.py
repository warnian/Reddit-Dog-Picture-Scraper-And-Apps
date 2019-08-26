##emails pupper pictures
"""
sends out an email on a regular basis of submissions grabbed off reddit from the pupperscraper
"""
import os, sys, inspect
import smtplib, time, email, io
from pupperScraper import pupperScraper
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


scraper = pupperScraper()

## gets emails from emails.txt
def get_email(in_file):
    emails = []
    with open (in_file, 'r', encoding = 'utf-8') as email_file:
        for email in email_file:
            emails.append(email)
    return emails

## creates the message to be sent
def message_generator():
    
    msg = MIMEMultipart()
    msg['Subject'] = 'Doggo of The Day, '+datetime.today().strftime('%Y-%m-%d')
    msg['From'] = 'Pupper Bot'
    pupper_tuple_list = scraper.pupperList

    ##attaches header to message
    with open ('header.txt','r',encoding = 'utf-8') as header_file:
        for line in header_file:
            msg.attach(MIMEText(line, 'plain'))
    for entry in pupper_tuple_list:
        
        msg.attach(MIMEText('\n'))
        msg.attach(MIMEText(entry[1],'plain'))
        msg.attach(MIMEText('<html><body><p><img src="'+entry[2]+'" width ="400"></p></body></html>','html','utf-8'))
    
    with open ('footer.txt','r',encoding = 'utf-8') as footer_file:
        for line in footer_file:
            msg.attach(MIMEText(line,'plain'))

    return msg
## main function which handshakes with email server and sends off message
def main():
    with open('secrets.txt', 'r') as secrets_file:
        secret = secrets_file.read()
    emails = get_email('emails.txt')  
    gmail_user = 'pupperemailer@gmail.com'
    message = message_generator()
    try:
        email_server_ssl = smtplib.SMTP_SSL(host ='smtp.gmail.com',port = 465)
        email_server_ssl.ehlo()
        email_server_ssl.login(gmail_user,secret)
        for email in emails:
            
            email_server_ssl.send_message(message,gmail_user,email)
        print ('emails sent')
    except:
        print('no email handshake...')

main()


