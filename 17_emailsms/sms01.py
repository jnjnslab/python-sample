from twilio.rest import Client

# 設定値
account_SID = 'xxx'
auth_token = 'xxx'
twilio_number = '+1xxxxxxxxxx' # 購入した米国の電話番号
my_number = '+8190xxxxxxxx'   # 自分の携帯電話番号

def textmyself(message):
    twilio_cli = Client(account_SID, auth_token)
    twilio_cli.messages.create(body=message, from_=twilio_number, to=my_number)


textmyself('SMSのテスト')