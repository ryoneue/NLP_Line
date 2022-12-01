# NLP_Line
## 概要
IOS版LINEアプリで保存したトーク履歴解析用スクリプト（開発途中）



![image](https://user-images.githubusercontent.com/24537884/200872920-c4b3f1db-5cfd-48cf-b0a4-2d8d9214bdd6.png)


## 現在開発済み機能
- ユーザ名ごとにワードカウント
- CSV形式で出力




## 準備
トーク履歴のtxtファイルをdataディレクトリ直下に格納（要utf8に変換）
ファイル名はmain.pyの--txt 引数で指定
## 使い方
```
$pip install -r requirements.txt
$pip install -r requirements_dev.txt 
$python main.py --txt data/sample.txt --model nlp
```

## 補足
MeCabのインストールでエラーが発生する場合は以下を参照
（特にUbuntuの場合は必須？）
https://virment.com/how-to-install-mecab-python-ubuntu/
