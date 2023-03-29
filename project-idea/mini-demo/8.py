#  自动发送邮件     
# 目的：编写一个Python脚本，可以使用这个脚本发送电子邮件。      
# 提示：email库可用于发送电子邮件。         

import smtplib
from email.message import EmailMessage

email = EmailMessage()  # create an object for EmailMessage     
email['from'] = 'xyz name'
email['to'] = 'xyz id'  
email['subject'] = 'xyz subject'    
email.set_content('xyz content of email')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:

    # send request to server
    smtp.ehlo()     # server object
    smtp.starttls()     # used to send data between server and client
    smtp.login("email_id", "psw")   #login
    smtp.send_message(email)    # send email
    print("email sent")





