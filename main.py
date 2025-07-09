from q6 import *
name=input("Enter your name: ")
marks=list(map(int,input("Enter your marks: ").strip().split()))
m=[]
for i in marks:
    if 0<=i<=100:
        m.append(i)
    else:
        print("Invalid mark enter between 0 and 100")
        exit()
print(f"Name :{name}")
print(f"Marks : {m}")
avge=avg(m)
print(f"Average is {avge}")
gra=val_grade(avge)
print(f"Grade is {gra}")