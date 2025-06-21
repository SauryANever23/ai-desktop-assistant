import smtplib 
import subprocesses 

class SendEmail():
    """This class is used to send emails"""
    def __init__(self):
        self.s = smptlib.SMPT('smpt.gmail.com', 587)
