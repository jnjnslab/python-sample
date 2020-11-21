import imapclient
import pyzmail

#GMailのIMAPサーバーにログインする
imap_obj = imapclient.IMAPClient('imap.gmail.com',use_uid=True)
imap_obj.login('xxx@gmail.com', 'xxx')

#フォルダーを選択する
imap_obj.select_folder('INBOX')
#検索を実行する
messages = imap_obj.search(['ALL'])  #全メールを返す
#messages = imap_obj.search(['FROM', 'xxx@gmail.com'])  #送信者で選択する

print('件数:' + str(len(messages)))
#メールを取得する
rawMessages = imap_obj.fetch(messages, ['BODY[]'])
for UID in rawMessages.keys():
    print(UID)
    # 生のメッセージを解析
    message = pyzmail.PyzMessage.factory(rawMessages[UID][b'BODY[]'])
    print(message.get_subject())
    print(message.get_address('from'))
    print(message.get_address('to'))
    print(message.get_address('cc'))
    print(message.get_address('bcc'))
    if message.html_part != None:
        body = message.html_part.get_payload().decode(message.html_part.charset)
        print(body)
    if message.text_part != None:
        body = message.text_part.get_payload().decode(message.text_part.charset)
        print(body)

#IMAPサーバーからの接続を切断する
imap_obj.logout()