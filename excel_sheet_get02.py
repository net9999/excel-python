import openpyxl as px
import os
import csv

#ファイルリストを読み込む
fi = os.listdir()

#出力する空の配列1，2を作成
li = []
li2 = []
#ファイルリストの要素について処理を行う
for y in fi:
    #ドットを使ってスプリット
    z = y.split(".")

    #リストの最後の値がxlsxか確認して処理を進める
    if z[-1] == "xlsx":

        #ファイル名をリストの先頭に入れる
        li.append(y)

        #ファイルを開きシート名を取得して，配列1に追加する
        bk = px.load_workbook(y)
        sn = bk.sheetnames
        li.extend(sn)


        #配列1を出力する配列2に追加
        li2.append(li)

        #for内の配列を空にする
        li = []

#print(li2)
#csvファイルを開き，保存，SHIFT-JISじゃないとうまくいかなかった
with open("stock.csv", "w", encoding="SHIFT-JIS") as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(li2)
