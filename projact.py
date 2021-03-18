"""
import sqlite3
conn = sqlite3.connect("peedata.db")
c = conn.cursor()
c.execute ('''CREATE TABLE s10 (id integer PRIMARY KEY AUTOINCREMENT,
    Fname varchar(30) NOT NULL,
    LName varchar(30) NOT NULL,
    score float(30) NOT NULL,
    time float(30) NOT NULL,
    sum float(30) NOT NULL)''')
conn.commit()
conn.close()
"""

import sqlite3
conn = sqlite3.connect("peedata.db")
c = conn.cursor()
def menu():
    global choice
    print('-'*5,'ระบบแข่งขันยิงปืน','-'*5)
    print('='*28,'\nเพิ่มข้อมูลสมัคร กด [a]\nแสดงข้อมูลผู้สมัคร [s]\nลงแข่งขัน [e]\nลบข้อมูลนักเรียน [d]\nออกจากระบบ [x]')
    choice = input('\nกรุณาเลือกทำรายการ :')
def show1():
    conn = sqlite3.connect("peedata.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM a1''')
    result = c.fetchall()
    print('{0:-<12}{1:-<15}{2:-<15}{3:-<27}{4:-<10}{5}'.format('ลำดับที่',' ชื่อ','สกุล','คลาส','ประเภท','ชื่อทีม'))
    for x in result :
        print('{0:<8}{1:<15}{2:<15}{3:<27}{4:<10}{5}'.format(x[0],x[1],x[2],x[3],x[4],x[5]))
    conn.commit()
    conn.close()

def show2():
    conn = sqlite3.connect("peedata.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM a2''')
    result = c.fetchall()
    print('{0:-<12}{1:-<15}{2:-<15}{3:-<27}{4:-<10}{5}'.format('ลำดับที่',' ชื่อ','สกุล','คลาส','ประเภท','ชื่อทีม'))
    for x in result :
        print('{0:<8}{1:<15}{2:<15}{3:<27}{4:<10}{5}'.format(x[0],x[1],x[2],x[3],x[4],x[5]))
    conn.commit()
    conn.close()


def add1(Fname,LName,calss,competition,nametame):
    try :
        conn = sqlite3.connect("peedata.db")
        c = conn.cursor()
        sql = '''INSERT INTO a1 (Fname,LName,calss,competition,nametame) VALUES (?,?,?,?,?)'''
        data = (Fname,LName,calss,competition,nametame)
        c.execute(sql,data)
        conn.commit()
        c.close()

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close() 

def add2(Fname,LName,calss,competition,nametame):
    try :
        conn = sqlite3.connect("peedata.db")
        c = conn.cursor()
        sql = '''INSERT INTO a2 (Fname,LName,calss,competition,nametame) VALUES (?,?,?,?,?)'''
        data = (Fname,LName,calss,competition,nametame)
        c.execute(sql,data)
        conn.commit()
        c.close()

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close() 
def s1(Fname,LName,score,time,sum):
    try :
        conn = sqlite3.connect("peedata.db")
        c = conn.cursor()
        sql = '''INSERT INTO s1 (Fname,LName,score,time,sum) VALUES (?,?,?,?,?)'''
        data = (Fname,LName,score,time,sum)
        c.execute(sql,data)
        conn.commit()
        c.close()

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close() 
def s2(Fname,LName,score,time,sum):
    try :
        conn = sqlite3.connect("peedata.db")
        c = conn.cursor()
        sql = '''INSERT INTO s1 (Fname,LName,score,time,sum) VALUES (?,?,?,?,?)'''
        data = (Fname,LName,score,time,sum)
        c.execute(sql,data)
        conn.commit()
        c.close()

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close() 
def s3(Fname,LName,score,time,sum):
    try :
        conn = sqlite3.connect("peedata.db")
        c = conn.cursor()
        sql = '''INSERT INTO s1 (Fname,LName,score,time,sum) VALUES (?,?,?,?,?)'''
        data = (Fname,LName,score,time,sum)
        c.execute(sql,data)
        conn.commit()
        c.close()

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close() 

while True:
    menu()
    if choice == 's':
        a = input('การุณาเลือกข้อมูลที่คุณต้องการ :')
        if a =='show1':
            show1()
        elif a == 'show2':
            show2()
    elif choice == 'a':
        a = input('การุณาเลือกลำทีมของท่าน :')
        if a == 'add1':
            x =int (input('ท่านมีผู้เล่นกี่คน : '))
            for i in range(x):
                a,b,c,d,e = input('ชื่อ-สกุล-คลาส-ประเภทการแข่งขัน-ชื่อทีม : ').split()
                add1(a,b,c,d,e)
        elif a == 'add2':
            x =int (input('ท่านมีผู้เล่นกี่คน : '))
            for i in range(x):
                a,b,c,d,e = input('ชื่อ-สกุล-คลาส-ประเภทการแข่งขัน-ชื่อทีม : ').split()
                add2(a,b,c,d,e)