#getメソッド
picnic_items = {'apples':5,'cups':2}
print(str(picnic_items.get('cups',0))) #辞書に存在する場合、値を返す
print(str(picnic_items.get('eggs',0))) #辞書に存在しない場合、0を返す