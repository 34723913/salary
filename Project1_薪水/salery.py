import datetime
now=datetime.datetime.now()
print(f"你好，歡迎來到月薪計算系統! 現在是 {now}")
def interval_month(): #區間月份
    d1 = input("請輸入區間1 yyyy/mm/dd:")
    d2 = input("請輸入區間2 yyyy/mm/dd:")
    wage=int(input("請輸入你的時薪:"))
    work_hours=int(input("請輸入你的工作小時:"))
    import pandas as pd #導入panda
    e =pd.bdate_range(d1,d2)
    #d1,d2開始/結束日期
    min=len(e)
    #len返回對象長度
    print(min*wage*work_hours)
interval_month()
