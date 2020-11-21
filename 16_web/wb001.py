import webbrowser
#webbrowserのopen関数でブラウザを開く

address = '新橋'
#ブラウザでGoogle Mapを開く
webbrowser.open('https://www.google.co.jp/maps/place/' + address)