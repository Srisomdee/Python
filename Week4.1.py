print('--------------การุณากรอกประวัติของคุณ-------------------')
a = str (input('Enter your namelastname :'))
b = int (input('Enter your year :'))
c = int (input('Enter your number :'))
t = str (input('Enter your branch :'))
d = str (input('Enter your sex :'))
e = str (input('Enter your province :'))
class nisit :
    def __init__ (self ,namelastname ,year ,number ,branch ,sex ,province) :
        self.namelastname = namelastname
        self.year = year
        self.number = number
        self.branch = branch
        self.sex = sex
        self.province = province
    def showstuden(self) :
        print('-------------------------แนะนำตัว--------------------')
        print('สวัสดีครับ')
        print('name :',self.name)
        print('year :',self.year)
        print('number :',self.number)
        print('branch :',self.branch)
        print('sex :',self.sex)
        print('province :',self.province)
x = nisit(a,b,c,t,d,e)
x.showstuden()

