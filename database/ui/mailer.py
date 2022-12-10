import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
Mailer class setups up an outgoing email account to allow applications to send mail from that account.

Usage:
    my_mailer = Mailer("py_mailer@email.com","secretpassword","smtp.email.com",587,True,True,False)
    my_mailer.send_mail("recipent@email.net", "Mail Subject", "Mail body text.")

    __init__()
        sender_address is the email account sending the email
        sender_password is the password to authenticate the sender account on the SMTP server
        smtp_server is the mail server that authenticates the mail account and delivers the email to the recipent's email server
        smtp_port_number is the port number the SMTP server has open for connections. Common SMTP port numbers are 25 and 587
        use_starttls if True, the program will attempt to connect to the SMTP server securely with starttls
        do_login if True, the program will attempt to authenticate with the SMTP server
        do_debug if True, the program will attempt to print informative status messages of the connection progress to standard out

    send_mail()
        receiver_address is the email address of the recipent
        mail_subject is the subject line of the email message
        mail_message is the text for the message body

        Function returns True if the message was sucessfully delivered to the outgoing SMTP server.


Notes:
    - Many ISP, like Comcast, block all outgoing SMTP connections not going through their SMTP server. With Comcast, you must authenticate against their 
        SMTP relay with your Comcast credencials to deliver the message.
    - If your ISP does not block SMTP ports, if you are using Gmail as your sender's email address, regular gmail accounts do not support connections from
        third part applications like this one unless the following criteria are satisfied:
            - It is a Google Workspaces account
            - The Google Workspaces administrator permits less secure logins for the domain
            - The Google Workspaces account has enabled less secure logins
"""
class Mailer:
    def __init__(self,
    sender_address = "sender@email.com",
    sender_password = "hunter2",
    smtp_server = "smtp.gmail.com", # for gmail accounts, it must be a Workspaces account and the workspace must permit "less secure apps" https://support.google.com/a/answer/176600?hl=en
    smtp_port_number = 587,
    use_starttls = True,
    do_login = True,
    do_debug = False):
        self.sender_address = sender_address
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port_number = smtp_port_number
        self.use_starttls = use_starttls
        self.do_login = do_login
        self.do_debug = do_debug

    def send_mail(self, receiver_address,
    mail_subject,
    mail_message):
        

        # MIME setup
        message = MIMEMultipart()
        message["From"] = self.sender_address
        message["To"] = receiver_address
        message["Subject"] = mail_subject
        message.attach(MIMEText(mail_message, 'plain'))

        text = message.as_string()

        # Sending the message
        try:
            # connect to smtp server
            session = smtplib.SMTP(self.smtp_server, self.smtp_port_number)
            if self.do_debug: print("session established")
            
            # if server is configured to use starttls, connect with starttls
            if self.use_starttls: 
                session.starttls()
                if self.do_debug: print("starttsl established")
            
            # if server requires login to send email (and it should!)
            if self.do_login: 
                session.login(self.sender_address, self.sender_password)
                if self.do_debug: print("login establisehd")
            
            # send the message from the sender to the receiver with the composed text
            session.sendmail(self.sender_address, receiver_address, text)
            if self.do_debug: print("message sent")
            
            # terminate the session
            session.quit()
            if self.do_debug: print("session closed")

            return True
        except:
            print("message not sent")
            return False


