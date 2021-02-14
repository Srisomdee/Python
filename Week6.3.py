import sqlite3
conn = sqlite3.connect(r"D:\python_matee\example.db")
c = conn.cursor()
def menu():
    global choice
    print('-'*5,'ระบบทะเบียนนักเรียน','-'*5)
    print('='*28,'\nเพิ่มข้อมูลนักเรียน กด [a]\nแสดงข้อมูลนักเรียน [s]\nแก้ไขข้อมูลนักเรียน [e]\nลบข้อมูลนักเรียน [d]\nออกจากระบบ [x]')
    choice = input('\nกรุณาเลือกทำรายการ :')

#คำสั่งโชว์รายชื่อในตาราง
def show():
    conn = sqlite3.connect(r"D:\python_matee\example.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM profile''')
    result = c.fetchall()
    for x in result :
        print(x)
    conn.commit()
    conn.close()

#คำสั่งเพิ่มข้อมูลลงตาราง
def add(fname,lName,email,Sex,Age,Gradelevel):
    try :
        conn = sqlite3.connect(r"D:\python_matee\example.db")
        c = conn.cursor()
        sql = '''INSERT INTO profile (fname,lName,email,sex,age,Gradelevel) VALUES (?,?,?,?,?,?)'''
        data = (fname,lName,email,Sex,Age,Gradelevel)
        c.execute(sql,data)
        conn.commit()
        c.close()

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()

#คำสั่งแก้ไขข้อมูลในตาราง
def modify ():
    try :
        m,s,u,t,h,i,p = input('ชื่อ-สกุล-อีเมล-เพศ-อายุ-ชั้นปี-แถวที่ : ').split()
        conn = sqlite3.connect(r"D:\python_matee\example.db")
        c = conn.cursor()
        data = ( m,s,u,t,h,i,p )
        c.execute('''UPDATE profile SET fname=?,lName=?,email=?,Sex=?,Age=?,Gradelevel=? WHERE id = ?''',data )
        print('แก้ไขข้อมูลเรียบร้อย')
        conn.commit()
        c.close()
    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()
 
#คำสั่งลบข้อมูลในตารางแบบระบุแถว
def delete ():

    try :
        drow = (input('ต้องการลบแถวที่ :'))
        conn = sqlite3.connect(r"D:\python_matee\example.db")
        c = conn.cursor()
        data = (drow)
        c.execute('DELETE FROM profile WHERE id = ?''',data)
        print('ลบข้อมูลเรียบร้อย')
        conn.commit()
        c.close ()
    except sqlite3.Error as e:
        print(e)
    finally :
        if conn :
            conn.close()
                                
while True:
    menu()
    if choice == 's':
        show()
    elif choice == 'a':
        a,b,c,d,e,f = input('ชื่อ-สกุล-อีเมล-เพศ-อายุ-ชั้นปี : ').split()
        add(a,b,c,d,e,f)
        print('เพิ่มข้อมูลเรียบร้อยแล้ว')
    elif choice == 'e':
        modify()
    elif choice == 'd':
        delete()
    elif choice == 'x':
        yesno = input('ต้องการออกจากระบบหรือไม่ [y/n]:')
        if yesno == 'Y' or yesno == 'y':
            print('ออกจากระบบเรียบร้อยแล้ว')
            break
        elif yesno == 'N' or yesno == 'n':
            print('ได้ทำการกลับสู่ระบบแล้ว')
            continue
        else:
            print('Fail!')

#การเพิ่มข้อมูลลงตาราง
"""
#c.execute('''INSERT INTO profile (id,fname,lName,email,Sex,Age,Gradelevel) VALUES (NULL,"maytee","Srisomdee","matee@kkumail.com","male","18","M.6")''')
#c.execute('''INSERT INTO profile VALUES (NULL,"Cawadon","Banjong","cawadon@kkumail.com","male","18","M.6")''')
#c.execute('''INSERT INTO profile VALUES (NULL,"Watcharachat","Asana","Watcharachat@kkumail.com","male","17","M.6")''')
#c.execute('''INSERT INTO profile VALUES (NULL,"Parin","Pukabpech","parin@kkumail.com","male","16","M.6")''')
#c.execute('''INSERT INTO profile VALUES (NULL,"Angkun","Kaeowanna","angkun@kkumail.com","male","18","M.6")''')
#c.execute('''INSERT INTO profile VALUES (NULL,"Akaradch","Thongngan","akaradch@kkumail.com","male","18","M.6")''')
#conn.commit()
#conn.close()

"""
#คำสั่งการเพิ่มข้อมูลแชื่อมต่อลงdata
"""import sqlite3 #import sqlite3
conn = sqlite3.connect("example.db")
c = conn.cursor() #create a cursor object 
c.execute ('''CREATE TABLE users(id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lName varchar(30) NOT NULL,
    email varchar(100) NOT NULL)''')
conn.commit()
conn.close()"""

