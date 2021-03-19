import sqlite3
conn = sqlite3.connect(r"D:\python_matee\projact_แก้\projact.db")
c = conn.cursor()
category = ["Open","Standard","Modify","Standard manual"]

def input_date():
    print('กรุณากรอกข้อมูลดั้งต่อไปปนี้')
    name = input('กรอกชื่อและนามสกุลของท่าน :')
    print('ประเภทของการแข่งขันมีดังนี้\n1.Open คือ ปืนลูกซองแบบแมกกาซีน\n2.Standard คือ ปืนออนโต้แบบไม่ได้แต่งปืน\n3.Modify คือ ปืนออโต้แบบติดดอท ใส่คอมพ์ลดแรงรีคอย\n4.Standard manual คือ ปืนลูกซองแบบปั้มไม่แต่งอะไร')
    p = int(input('กรุณาเลือกประเภทของท่าน :'))
    co = category[p+1]
    s = input('กรุณาเลือกลำดับกลุ่มของท่าน(1-5):')
    date = (name,"U",s,0,0,0,0,0,0,0,0,0,0,"0",co)
    c.execute('INSERT INTO gun (Name,Level,Groupp,Field1,Field2,Field3,Field4,Field5,Field6,Field7,Field8,Field9,Field10,Scoresum,Typell) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',date)
    conn.commit()
    c.close()

def show():
    print('กรุณาเลือกดูข้อมูล\nดูทั้งหมดกด[1]\nเฉพาะข้อมูลของท่านกด[2]')
    information = int(input('กรุณาเลือกหมายเลขของท่าน :'))
    if information == 1:
        c = conn.cursor()
        c.execute('''SELECT * FROM gun''')
        result = c.fetchall()
        print("{0:-<30}{1:-<20}{2:-<10}{3:-<20}{4:-<7}{5:-<7}{6:-<7}{7:-<7}{8:-<7}{9:-<7}{10:-<7}{11:-<7}{12:-<7}{13:-<7}{14:-<10}".format("ชื่อ-นามสกุล","ประเภทที่เล่น","เลเวล","กลุ่มที่อยู่","รอบ1","รอบ2","รอบ3","รอบ4","รอบ5","รอบ6","รอบ7","รอบ8","รอบ9","รอบ10","คะแนนรวม"))
        for x in result:
            if x[3] != 0:
                print("{0: <30}{1: <20}{2: <10}{3: <20}{4: <7}{5: <7}{6: <7}{7: <7}{8: <7}{9: <7}{10: <7}{11: <7}{12: <7}{13: <7}{14: <10}".format(x[0],x[14],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13]))
            else:
                print("{0: <30}{1: <20}{2: <10}{3: <20} ยังไม่มีการกรอกคะแนน!".format(x[0],x[14],x[1],x[2]))
    else:
        name = input("พิมพ์ชื่อและนามสกุลที่คุณต้องการค้นหา: ")
        name_o = (name)
        c = conn.cursor()
        c.execute(' SELECT * FROM gun WHERE Name = ?',(name_o,))
        if c.fetchone():
            c.execute(' SELECT * FROM gun WHERE Name = ?',(name_o,))
            result = c.fetchall()
            print(x)
            for x in result:
                print("ชื่อ-นามสกุล: "+str(x[0])+"\nประเภทที่เล่น: "+str(x[14])+"\nเลเวล: "+str(x[1])+"\nกลุ่มที่:"+str(x[2])+"\nคะแนนทั้ง10รอบ\n{0:-<7}{1:-<7}{2:-<7}{3:-<7}{4:-<7}{5:-<7}{6:-<7}{7:-<7}{8:-<7}{9:-<7}{10}".format("รอบ1","รอบ2","รอบ3","รอบ4","รอบ5","รอบ6","รอบ7","รอบ8","รอบ9","รอบ10","คะแนนรวม"))
                x = str(x)
                if x[3]!=0:
                    print("{0:-<7}{1:-<7}{2:-<7}{3:-<7}{4:-<7}{5:-<7}{6:-<7}{7:-<7}{8:-<7}{9:-<7}{10}".format(str(x[3]),str(x[4]),str(x[5]),str(x[6]),str(x[7]),str(x[8]),str(x[9]),str(x[10]),str(x[11]),str(x[12]),str(x[13])))
                else:
                    print("ยังไม่ลงไม่มีคะแนน!")
        else:
            print("ไม่พบชื่อของคุณ")

def 
print('ยินดีต้อนรับเข้าสู่โปรแกรมยิงปืน\nกรุณาเลือกรายการดั้งต่อไปนี้\nกด[1].ลงทะเบียน\nกด[2].ดูข้อมูลของท่าน\nกด[3].กรอกคะแนนการแข่งขัน\nกด[4].ออกจากระบบ')
a = int(input('กรุณากรอกตัวเลือกของท่าน :'))
if a == 1:
    input_date()
elif a == 2:
    show()