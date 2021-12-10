import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com',0)

server.ehlo()

with open('password.txt','r')as f:
    password = f.read()

server.login('smth@gmail.com',password)

msg = MIMEMultipart()
msg['From'] = 'MysticSlice'
msg['To'] = 'smth2@gmail.com'
msg['Subject'] = 'Just A Test'

with open('message.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message,'plain'))

filename = 'hi.jpg'
attachment = open(filename,'rb')

p = MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment',filename = '{filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('smth@gmail.com','smth2@gmail.com',text)
print("Mail Sent")
attachment.close()
