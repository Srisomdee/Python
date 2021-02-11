print('-'*30)
print('       ร้านอิ่มใจอาหารตามสั่ง')
print('-'*30)
print('1. แสดงรายการสินค้ากด a')
print('2.เพิ่มรายการสินค้ากด b') 
print('3.ออกจากระบบกด c')
a = input('การุณาเลือกทำรายการ :')
print('-'*30)    

class shop :
    def __init__ (self ,namestore ,goods ) :
        self.namestore = namestore
        self.goods = goods
    def showfood(self) :
        print('ชื่อร้าน :',self.namestore)
        print('รายการอาหาร :\n',self.goods)
class goodsnew :
    def __init__ (self ,namestore ,goods) :
        super().__init__(namestore ,goods)
        self.adduser = adduser
x = shop('ร้านอิ่มใจอาหารตามสั่ง','1.กระเพราหมูกรอบ ราคา 20 บาท \n'+ '2.กระเพราะไก่กรอบ ราคา 40 บาท\n'+
 '3.ผัดเผ็ด ราคา 50 บาท\n'+'4.แกงจืด ราคา 60 บาท' ,'s' )
print(x.adduser)
x.showfood()

while True:
    menu()
    if choice == 'a':
        shop()
    elif choice == 'b':
        goodsnew()
    '''elif choice == '3':
        delete()
    else:
        yesno2=input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n : ')
        if yesno2 == 'y':
            break
        elif yesno2 == 'n':
            continue'''
