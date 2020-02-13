import openpyxl as px
import os

#ファイルリストを読み込む
fi = os.listdir()

#出力する空の配列を作成
li = []

#ファイルリストの要素について処理を行う
for y in fi:
    #ドットを使ってスプリット
    z = y.split(".")

    #リストの最後の値がxlsxか確認して処理を進める
    if z[-1] == "xlsx":

        #ファイル名をリストの先頭に入れる
        li.append(y)

        #ファイルを開きシート名を取得して，配列に追加する
        bk = px.load_workbook(y)
        sn = bk.sheetnames
        li.extend(sn)

        #配列を出力
        print(li)

        #配列を空にする
        li = []
