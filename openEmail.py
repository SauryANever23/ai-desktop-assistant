import smtplib 
import os

class SendEmail():
    """This class is used to send emails"""
    
    @staticmethod
    def send(message, reciever):
        # create an smtp session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication 
        s.login(os.environ["EMAIL_ID"], os.environ["EMAIL_ID_PASS"])

        # message that is to be sent 
        payload = f"{message}"

        s.sendmail(os.environ["EMAIL_ID"], reciever, payload)

        s.quit()

def main():
    SendEmail.send("I am sending this using SMTPlib", "mukeshkumarjha98@gmail.com")

if __name__ == '__main__':
    main()






