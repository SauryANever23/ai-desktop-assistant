from email.message import EmailMessage 
import smtplib 
import os

class SendEmail():
    """This class is used to send emails"""
    
    @staticmethod
    def send(message: str, subject: str, reciever: str) -> None:
        payload = EmailMessage()
        payload.set_content(f"{message}") # sending the content 
        payload["Subject"] = subject
        payload["From"] = os.environ["EMAIL_ID"]
        payload["To"] = reciever

        with smtplib.SMTP_SSL('smtp.gmail.com', 587) as s:
            s.starttls() # Transport layer security 
            s.login(os.environ["EMAIL_ID"], os.environ["EMAIL_ID_PASS"]) # Logging in 
            s.send_message(payload)
            

def main():
    message = """
    ## I want you to make my computer work
    - For that reason lets go make it, after lunch
    """
    SendEmail.send(message, "Computer" "mukeshkumarjha98@gmail.com")

if __name__ == '__main__':
    main()






