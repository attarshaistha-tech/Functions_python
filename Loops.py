#loops in python
#1.for loop
for i in range(5):
    print(i)

fruits=["apple","banana","lichi"]
for i in fruits:
    print(i)

names=["attar","mass","sai","kavi"]
for i in range(len(names)):
    print(i,names)

#2.while loop
count=1
while count<=5:
    count+=1
    print(count)

#incrementing series
count=1
while count<=5:
    print(count)
    count+=1

#decrementing series
count=5
while count>=1:
    print(count)
    count-=1

count=5
while count>=1:
    count-=1
    print(count)

#conditions through "and","not","or,"ternary operator"
#and
age=20
if age>=18 and age<=60:
    print("eligible to vote")

#or
age=20
if age>18 or age>60:
    print("not eligible to vote")

#not
skills={"python","java","sql"}
print("python" in skills) #true
#if "python" not in skills:
    #print("not eligible for python job")

#ternary operator
cgpa=8.5
results="prathibha" if cgpa>=8 else "needs improvement"
print(results)

#Types of looping statements
#1.list looping
skills=["python","java","sql","aws"]
for skill in skills:
    print(skill)

l=[1,2,3,4,5]
L=[11,21,31,41,51]
D=[20,21,2,33,44]
S={'A':"apple",'B':"banana",'C':"lichi"}
for i in range(len(l)):
    print(l[i])
    #print(i)
    print(S)
    print(S.get(i))
    #print(S[i])

#2.nested looping
students=[["prathibha","sai","kavi"],
            ["python","java","sql"]]
for i in students:
    for j in i:
        print(j)
        print(i)

#LOOP THROUGH CONTROL STATEMENTS
#1.BREAK
for i in range(10):
    if i==5:
        break
    print(i)

#2.CONTINUE
for i in range(10):
    if i==5:
        continue
    print(i)