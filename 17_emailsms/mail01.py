import smtplib, sys
from email.mime.text import MIMEText
from email.header import Header

# GMailのSMTPサーバーにログインする
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login('xxx@gmail.com', 'xxx') #Google のIDとパスワード
#メールを送信する
from_address = 'xxx@gmail.com'
to_address = 'xxx@gmail.com'
msg = MIMEText(u'日本語の本文')
msg['Subject'] = Header(u'日本語の件名')

sendmail_status = smtp_obj.sendmail(from_address, to_address, msg.as_string())
print(sendmail_status)

smtp_obj.quit()