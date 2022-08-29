import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

Success = 0
Failed = 1

# sender email address : pytracker.sender@hotmail.com
# sender email password: pytracker_sender

# receiver email address : pytracker.receiver@hotmail.com
# receiver email password: pytracker_receiver

username = "pytracker.sender@hotmail.com"
password = "pytracker_sender"

mail_from = "pytracker.sender@hotmail.com"
mail_to = "pytracker.receiver@hotmail.com"

global feedback_info
feedback_info = None

connection = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)

def send_email():
    if feedback_info == None:
        print("You need to have feedback information!!")
        return Failed
    fname, lname, issue_type, feedback_msg = feedback_info["first_name"],feedback_info["last_name"],feedback_info["issue-type"],feedback_info["feedback_message"]
    
    mail_subject = f"Pytracker Feedback from {fname} {lname}"
    mail_body = f"issue_type : {issue_type}\nfeedback_message : {feedback_msg}"
    
    mimemsg = MIMEMultipart()
    mimemsg['From'] = mail_from
    mimemsg['To'] = mail_to
    mimemsg['Subject'] = mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))
    
    connection.starttls()
    connection.login(username, password)
    connection.send_message(mimemsg)
    connection.quit()
    
    return Success