import imapclient

#GMailのIMAPサーバーにログインする
imap_obj = imapclient.IMAPClient('imap.gmail.com',use_uid=True)
imap_obj.login('xxx@gmail.com', 'xxx')
#フォルダーを選択する
imap_obj.select_folder('INBOX')
#検索を実行する
messages = imap_obj.search(['ALL'])  #全メールを返す
#IDのリストを表示する
print(messages)
#メールを削除する
imap_obj.delete_messages([23])
imap_obj.expunge()
#IMAPサーバーからの接続を切断する
imap_obj.logout()