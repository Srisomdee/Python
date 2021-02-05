print('โปรแกรมคำนวณเกรดนักเรียน')
print('-'*30)
print('กรุณากรอกคะแนนของท่าน')
print('-'*30)
a = int(input('Enter your score :'))
if a>=80 and a<=100 :
    print('A')  
elif a>=70 and a<=79 :
    print('B')
elif a>=60 and a<=69 :
    print('C')
elif a>=50 and a<=59 :
    print('D')
else :
    print('F')