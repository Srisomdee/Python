"""import sqlite3 #import sqlite3
conn = sqlite3.connect("example.db")
c = conn.cursor() #create a cursor object 
c.execute ('''CREATE TABLE users(id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lName varchar(30) NOT NULL,
    email varchar(100) NOT NULL)''')
conn.commit()
conn.close()"""
#คำสั่งการเพิ่มข้อมูลแชื่อมต่อลงdata

#คำสั้งใส่ข้อมูลลงตาราง
"""import sqlite3
conn = sqlite3.connect(r"D:\python_matee\example.db")
c = conn.cursor()
c.execute('''INSERT INTO users (id,fname,lName,email) VALUES (NULL,"maytee","Srisomdee","matee@kkumail.com")''')
c.execute('''INSERT INTO users VALUES (NULL,"Panarat","Numcha","Panarat@kkumail.com")''')
c.execute('''INSERT INTO users VALUES (NULL,"Watcharacat","Rsana","Watcharacat@kkumail.com")''')
c.execute('''INSERT INTO users VALUES (NULL,"Parin","Pugabpach","Parin@kkumail.com")''')
c.execute('''INSERT INTO users VALUES (NULL,"Cawadon","Banjong","Cawadon@kkumail.com")''')
conn.commit()
conn.close()"""

#คำสั่งแสดงผลข้อมูลจากตาราง
"""import sqlite3
conn = sqlite3.connect(r"D:\python_matee\example.db")
c = conn.cursor()
c.execute ('''SELECT * FROM users''')
result = c.fetchall()
for x in result :
    print(x)"""

#คำสั่งลบข้อมูลตามบรรทัด id = 7,id = 6
"""import sqlite3
conn = sqlite3.connect(r"D:\python_matee\example.db")
c = conn.cursor()

try :
    c.execute('DELETE FROM users WHERE id = 7')
    c.execute('DELETE FROM users WHERE id = 6')
    conn.commit()
    c.close ()

except sqlite3.Error as e:
    print(e)

finally :
    if conn :
        conn.close()"""   
                                    



import sqlite3 #import sqlite3
conn = sqlite3.connect("example.db")
c = conn.cursor() #create a cursor object 
"""c.execute ('''CREATE TABLE users(id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lName varchar(30) NOT NULL,
    email varchar(100) NOT NULL,
    Sex varchar(10) NOT NULL,
    Age varchar(10) NOT NULL,
    Grade level(20) NOT NULL)''')"""
conn.commit()
conn.close()


"""c.execute ('''CREATE TABLE users(id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lName varchar(30) NOT NULL,
    email varchar(100) NOT NULL,
    Sex varchar(10) NOT NULL,
    Age varchar(10) NOT NULL,
    Grade level(20) NOT NULL)''')"""
c.execute('''INSERT INTO users (id,fname,lName,email,Sex,Age,Grade) VALUES (NULL,"maytee","Srisomdee","matee@kkumail.com","male","18","M.6")''')
c.execute('''INSERT INTO users VALUES (NULL,"Panarat","Numcha","Panarat@kkumail.com","female","18","M.6")''')
c.execute('''INSERT INTO users VALUES (NULL,"Watcharacat","Asana","Watcharacat@kkumail.com","male","18","M.6")''')
c.execute('''INSERT INTO users VALUES (NULL,"Parin","Pugabpach","Parin@kkumail.com","male","17","M.6")''')
c.execute('''INSERT INTO users VALUES (NULL,"Cawadon","Banjong","Cawadon@kkumail.com","male","17","M.6")''')
