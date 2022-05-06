from datetime import date
sdate=[20,19,21,20,21,22,23,23,23,24,23,22] #
legal = False
counts=["摩羯座","水瓶座","雙魚座","白羊座","金牛座","雙子座","巨蟹座",'獅子座','處女座','天秤座','天蠍座','射手座']
birth = input().strip(' ')
cbir = birth.split('-')
cmonth = str(cbir[1])
cdate = str(cbir[2])
leap = False
month1 = {1, 3, 5, 7, 8, 10, 12}
month2 = {4, 6, 9, 11}
def sign(cmonth,cdate):
    if int(cdate) < sdate[int(cmonth)-1]:
        print(counts[int(cmonth)-1])
    else:
        print(counts[int(cmonth)])
        if  birth% 4 == 0 and birth % 100 != 0 or birth % 400 == 0:
            leap = True
        if birth in month1:
            if 1 <= day <= 31:
                legal = True
        elif birth in month2:
            if 1 <= day <= 30:
                legal = True
        elif birth == 2:
            if not leap and 1 <= day <= 28:
                legal = True
            elif leap and 1 <= day <= 29:
                legal = True
            if birth != True:
                print("Error")

sign(cmonth,cdate)



