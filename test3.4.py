student = int(input("จำนวนนักเรียน:"))
print("-"*30)
point_grade = [0 , 0 , 0 , 0 , 0 , 0]
score_grade = ["90-100 :","80-89 :","70-79 :","60-69 :","50-59 :","0-49 :"]
x = 0 
while x <= student :
    point = int(input("จำนวนคะแนนนักเรียน :"))
    if point <= 100 and point >= 90 :
        point_grade[0] += 1 
    elif point < 90 and point >= 80 :
        point_grade[1] += 1 
    elif point < 80 and point >= 70 :
        point_grade[2] += 1
    elif point < 70 and point >= 60 :
        point_grade[3] += 1
    elif point < 60 and point >= 50 :
        point_grade[4] += 1
    elif point < 50 and point >= 0 :
        point_grade[5] += 1 
        x+=1
for x in range(0,6) :
    print(score_grade[x],"*"*point_grade[x])
 