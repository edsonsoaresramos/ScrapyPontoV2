# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import smtplib
import imaplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.header import Header
import time
import datetime
import sys


EMAIL_ACCOUNT = "r3im0z@gmail.com"

# Use 'INBOX' to read inbox.  Note that whatever folder is specified,
# after successfully running this script all emails in that folder
# will be marked as read.
EMAIL_FOLDER = "inbox"

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "r3im0z" + ORG_EMAIL
FROM_PWD    = emailPwd
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def checkEmail(emailPwd):
    try:
        SMTP_SERVER = 'imap.gmail.com'
        SMTP_PORT = 993

        fromEmail = 'r3im0z@gmail.com'
        password = emailPwd

        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(fromEmail, password)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()

        first_email_id = int(id_list[0])
        last_email_id = int(id_list[-1])
        #for i in range(last_email_id, first_email_id, -1):
        for i in data[0].split():
            type, data = mail.fetch(i, '(RFC822)')

            for response in data:
                msg = mail.message_from_string(data[0][1])
                subject = msg['subject']
                emailFrom = msg['from']
                print('De: ' + emailFrom + '\n')
                print('Tema: ' + subject + '\n')
    except(Exception):
        print(str(Exception))
    except (imaplib.IMAP4.error):
        print('Error al logar')

def process_mailbox(M):
    """
    Do something with emails messages in the folder.
    For the sake of this example, print some headers.
    """

    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        print("No messages found!")
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", num)
            return

        msg = M.message_from_string(data[1])
        hdr = M.header.make_header(M.header.decode_header(msg['Subject']))
        subject = str(hdr)
        print('Message %s: %s' % (num, subject))
        print('Raw Date:', msg['Date'])
        # Now convert to local date-time
        date_tuple = M.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                M.utils.mktime_tz(date_tuple))
            print ("Local Date:", \
                local_date.strftime("%a, %d %b %Y %H:%M:%S"))


# M = imaplib.IMAP4_SSL('imap.gmail.com')
#
# try:
#     rv, data = M.login(EMAIL_ACCOUNT, emailPwd)
# except imaplib.IMAP4.error:
#     print ("LOGIN FAILED!!! ")
#     sys.exit(1)
#
# print(rv, data)
#
# rv, mailboxes = M.list()
# if rv == 'OK':
#     print("Mailboxes:")
#     print(mailboxes)
#
# rv, data = M.select(EMAIL_FOLDER)
# if rv == 'OK':
#     print("Processing mailbox...\n")
#     process_mailbox(M)
#     M.close()
# else:
#     print("ERROR: Unable to open mailbox ", rv)
#
# M.logout()


def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = mail.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print ('From : ' + email_from + '\n')
                    print ('Subject : ' + email_subject + '\n')

    except (Exception):
        print (str(Exception))

#checkEmail()
read_email_from_gmail()