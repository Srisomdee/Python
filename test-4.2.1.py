import os 
price = [50,100,200,350,1000,2000]
pee =[1,2,4,5,10,20]
good = [0,0,0,0,0,0]
def product():
    print(" รายการสินค้า\n",20*"-")
    for i in range(6):
        print(i+1,"มีดปราบผี",pee[i],'เล่ม', " ราคา",price[i],"บาท")

def choose():
    for i in range(6):
        print(i+1,"มีดปราบผี",pee[i],"เล่ม")
    data1 = int(input("กรุณาเลือกหยิบสินค้าหมายเลข :"))
    for i in range(6):
        if data1 == i+1:
            good[i] +=1

def show():
    sumz = 0
    sumx = 0 
    print(" ___สินค้าของคุณที่หยิบมีดังนี้___\n---สินค้า",17*"-"+"จำนวน",10*"-"+"ราคา---")
    for i in range(6):
        sumz = sumz+good[i]
        sumx = sumx+(good[i]*price[i])
        if good[i] > 0:
            print("มีดปราบผี",pee[i]," เล่ม",6*"-",good[i],12*"-",good[i]*price[i])
    print("รวม",23*"-",sumz,12*"-",sumx)
while(True):
    print(" โปรแกรมขายมีดปราบผีราคาเบาๆ \n",25*"-")
    print("1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.จำนวนและราคาสินค้าที่หยิบ\n 4.ปิดโปรแกรม\n")
    data = int(input("กรุณาลือกทำรายการ"))
    if data == 1:
        os.system("cls")
        product()
    elif data == 2 :
        os.system("cls")
        choose()
    elif data == 3 : 
        os.system("cls")
        show()
    else : 
        os.system("cls")
        out = input("คุณต้องการออกจารโปรแกรมใช่ไหม (y / n) :")
        if out == "y" :
            print("ขอบคุณที่ท่านมาใช้บริการ")
            break