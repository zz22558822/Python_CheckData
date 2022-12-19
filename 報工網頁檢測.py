import tkinter #GUI介面
import tkinter.messagebox #跳出TextBox使用
from datetime import date #載入當前時間使用
from datetime import datetime #載入日期格式時使用
import json #導入JSON
import requests #導入req請求



# ------------變數宣告區------------
ErrorNum = 0 #錯誤數量
YesNum = 0 #正確數量
NowDay = date.today() # 當前時間
# ---------------------------------



# ----------較為完善的爬蟲----------
# 定義資料網址
url = "http://iswd.avertronics.com/app01/SimisOnProgress.json"
# 模仿瀏覽器的標題
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}
# 使用Get()獲取資訊
html_response = requests.get(url=url, headers = headers)
# ---------------------------------




# ----------時間處理與判斷----------
# 獲取資訊帶入變數
r = requests.get(url) #將此頁面的HTML GET下來
data = json.loads(r.text)

# 迴圈篩選人員、日期
for i in data:
    # DeBug使用
    # print("人員名稱:" + i['人員名稱'])
    # print("生產日期:" + str(i['生產日期']))

    # 結束時間
    dateDay = datetime.date(datetime.strptime(i['生產日期'],'%Y/%m/%d'))# 將字串轉為時間格式僅留日期

    # 比對資料
    if dateDay != NowDay or dateDay > NowDay:
        ErrorNum = ErrorNum + 1
    else:
        YesNum = YesNum + 1


# 判斷錯誤數量超過 15筆
if ErrorNum >= 15:
    tkinter.messagebox.showerror('錯誤','報工網頁無刷新，請即刻檢查JSON資料狀態。')
else:
    tkinter.messagebox.showinfo('正常','目前資料正確。')





# # Debug使用 顯示所有資料
# print('錯誤數量: ' , ErrorNum)
# print('正確數量: ', YesNum)
# print('JSON時間: ', dateDay)
# print('當前時間: ', NowDay)
# print('是否相符: ', dateDay == NowDay)