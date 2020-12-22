import pandas as pd
#CSVファイルからDataFrameを作成する
person=pd.read_csv('data/survey_person.csv')
site=pd.read_csv('data/survey_site.csv')
survey=pd.read_csv('data/survey_survey.csv')
visited=pd.read_csv('data/survey_visited.csv')
#キーを指定して結合する、左のキーを全て残す
#how left 左のキーを全て残す
#    right 右のキーを全て残す
#    outer 左と右のキーを全て残す
#    inner 左右両方に存在するキーのみ残す
merged = visited.merge(site, left_on='site', right_on='name',how='left')
print(merged)