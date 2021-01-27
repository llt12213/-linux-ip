 #!/usr/bin/python

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
email_host = 'smtp.xx.com' #邮件服务器
email_port = 25
email_passwd = 'sdgugeercfhxdbah' #smtp授权码

sender = 'xxxxxxx@xx.com' #发件邮箱
receivers = ['xxxxxxx@xx', 'xxxxxxx@xx'] #收件邮箱
msg = MIMEMultipart()
msg['Subject'] = 'Dr_Li的邮件' #邮件主题
msg['From'] = sender
msg['To'] = ';'.join(receivers)

msg_text = MIMEText(_text='Hi, This email come from your Linux server', _subtype='plain', _charset='utf-8') #邮件文本
msg.mailach(msg_text)

mail = MIMEText(_text=open('./mail.txt', 'rb').read(), _subtype='base64', _charset='utf-8') #邮件附件
mail['Content-Type'] = 'application/octet-stream'
mail['Content-Disposition'] = 'mailachment; filename="mail.txt"'
msg.mailach(mail)

try:
   smtpObj = smtplib.SMTP(host=email_host, port=email_port)
   smtpObj.login(sender, email_passwd)
   smtpObj.sendmail(sender, receivers, msg.as_string())
   print("Successfully sent email")
   smtpObj.close()
except smtplib.SMTPException as e:
   print("Error: unable to send email")
   print(e)
