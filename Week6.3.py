import sqlite3
conn = sqlite3.connect(r"D:\python_matee\example.db")
c = conn.cursor()
while True:
    print("-----ระบบทะเบียนนักเรียน-----")
    print("========================================")
    print("เพิ่มนักเรียน กด[a]")
    print("แสดงข้อมูลนักเรียน [s]")
    print("แก้ไขข้อมูลนักเรียน[e]")
    print("ลบข้อมูลนักเรียน[d]")
    print("ออกจากโปรแกรม[x]")
    a  = input("กรุณาเลือกทำรายการ :")
    if a == a:
   
        def insertTousers(fname,lName,email,Sex,Age,Gradelevel) :
    
            try :  
                n = input('กรุณากรอกชื่อ :')     
                b = input('นามสกุล :')
                e = input('อีเมล :') 
                s = input('เพศ :')
                w = input('อายุ :') 
                g = input('ระดับชั้น :')        

                sql = '''INSERT INTO profile (fname,lName,email,Sex,Age,Gradelevel) VALUES (?,?,?,?,?,?)'''
                data = (fname,lName,email,Sex,Age,Gradelevel) 
                c.execute(sql,data)
                conn.commit ()
                c.close ()
                print("             เพิ่มเรียบร้อย")
            except sqlite3.Error as e:
                print('Failed to insert : ',e)
            finally :

                if conn :
                    conn.close ()
        insertTousers = (n,b,e,s,w,g)        
    



#c.execute('''INSERT INTO profile (id,fname,lName,email,Sex,Age,Gradelevel) VALUES (NULL,"maytee","Srisomdee","matee@kkumail.com","male","18","M.6")''')
#c.execute('''INSERT INTO profile VALUES (NULL,"Cawadon","Banjong","cawadon@kkumail.com","male","18","M.6")''')
#c.execute('''INSERT INTO profile VALUES (NULL,"Watcharachat","Asana","Watcharachat@kkumail.com","male","17","M.6")''')
#c.execute('''INSERT INTO profile VALUES (NULL,"Parin","Pukabpech","parin@kkumail.com","male","16","M.6")''')
#c.execute('''INSERT INTO profile VALUES (NULL,"Angkun","Kaeowanna","angkun@kkumail.com","male","18","M.6")''')
#c.execute('''INSERT INTO profile VALUES (NULL,"Akaradch","Thongngan","akaradch@kkumail.com","male","18","M.6")''')
#conn.commit()
#conn.close()"""

