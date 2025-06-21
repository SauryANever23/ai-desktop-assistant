from email.message import EmailMessage 
import smtplib 
import os

class SendEmail():
    """This class is used to send emails"""
    
    @staticmethod
    def send(message: str, subject: str, reciever: str) -> None:
        payload = EmailMessage()
        msg.set_content(f"{message}") # sending the content 
        msg["Subject"] = subject
        msg["From"] = os.environ["EMAIL_ID"]
        msg["To"] = reciever

        with smtplib.SMTP_SSL('smtp.gmail.com', 587) as s:
            s.starttls()
            
        

def main():
    SendEmail.send("I am sending this using SMTPlib", "mukeshkumarjha98@gmail.com")

if __name__ == '__main__':
    main()






