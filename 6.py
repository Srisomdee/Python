x = 25 
print('จ่ายแบบเหมาจ่าย กด 1')
print('จ่ายแบบจ่ายเพิ่ม กด 2')
a = int(input('Enter your number 1 or 2 :'))
s = int(input('กรุณากรอกระยะทาง(km) :'))
if a==1 :
    if s < 25:
        print('25 บาทครับ')
    else:
        print('80 บาทครับ')
if a==2 :
    if s < 25:
        print('25 บาทครับ')
    else:
        print('55 บาทครับ')