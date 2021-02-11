print('เลือกเมนูเพื่อทำรายการ')
print('######################')
print('ถ้ากด1 จะเป็นแบบจ่ายเพิ่ม')
print('ถ้ากด2 จะเป็นแบบเหมาจ่าย')
a = int (input ('enter manu 1 or 2 :'))
b = int (input ('enter your Distance (km):'))
s=25
if a==1:   
    #b = int (input ('enter your Distance (km):'))
    if  b <= 25:
        print('25')
    elif b > 25:
        print('55')
if a==2:
    if b > 25:
        print('80')
    elif b<=25:
        print('25')

       
            
'''a = int(input('กรุณากรอกจำนวนครั้งการรับค่า :')) 
i= 1
c= 0
while(i<=a):
    s = int(input('กรอกตัวเลข'))
    c = c+s   
    i+=1
print('ผลรวมทั้งหมด',c)'''

