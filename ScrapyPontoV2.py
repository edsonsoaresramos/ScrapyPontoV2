import smtplib
import time
import imaplib
import email

SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def readmail(emailAddress, pwd):
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(emailAddress, pwd)
        mail.select('inbox')
        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()

        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id, first_email_id, -1):
            typ, data = mail.fetch(str(i), '(RFC822)')

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(str(response_part[1]))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + str(email_from) + '\n')
                    print('Subject : ' + str(email_subject) + '\n')
    except(Exception):
        print(str(Exception))

readmail('r3im0z@gmail.com', '50p#144rt#ur')