# basic-class-12th

#FUNCTION THAT TAKES 3 VALUES AS PARAMETER AND RETURN THE MAXIMUM NO.
'''
def maximum(x,y,z) :
    if x>y and y>z:
        val= x
    elif x<y and y<z:
        val=z
    else:
        val=y
    return val
print(maximum(34,45,52))
'''

#TAKES A NO. AS A PARAMETER AND RETURN ITS FACTORIAL
'''
def fact(x):
    i=1
    for j in range(1,x+1):
        i = i*j
    return i
print(fact(5))
'''

#ACCESSING GLOBAL VARIABLE INSIDE A FUNCTION (GLOBAL KEYWORD)

'''
x=55
def foo():
    global x
    x=66
    print("LOCAL x : " , x)
foo()
print("GLOBAL x : ", x)
'''

#READ A FILE student.txt AND COUNT THE NO. OF CONSONENT IN IT.

'''
f_o = open("student.txt","r")
r=f_o.read()
c=0
for i in r:
    if i.lower() not in "aeiou" :
        c=c+1
print("NO. OF CONSONENT =",c)
f_o.close()
'''

#EXAMPLE OF SEEK

'''
f=open("alpha.txt","r")
print(f.read(4))
f.seek(2,0)
print(f.read())
f.close()
'''

#WAP TO READ A FILE ANSWER.TXT AND PRINT ALL THE WORDS SEPRATED BY "#"

'''
f = open("ANSWER.txt","r")
r=f.read().split()
for i in r:
    if "#" in i :
        print(i)
f.close()
'''

#WRITE A FUNCTION readme() WHICH ACCEPT THE LINE AS AN ARGUMNET AND PRINT
#THE FREQUENCY OF WORD india IN IT.

'''
c=0
def readme():
    global c
    f=open("text.txt","r")
    for i in f.read().split():
        if i.lower() == "india":
            c+=1
    return c
    f.close()
print(readme())
'''

#READ A FILE poem.txt AND PRINT ONLY THOSE LINES WHO'S LENGTH IS GREATER THAN 5 CHR

'''
f=open("poem.txt","r")
for i in f.readlines():
    if len(i)> 5 :
        print(i)
f.close()
'''

#WAF IN PY TO READ A TEXT FILE alpha1.txt AND DISPLAY THOSE LINE WHICH BEGAIN WITH
# "you"

'''
def you():
    f=open("alpha1.txt","r")
    for i in f.readlines():
        if i.split()[0].lower() == "you":
            print(i)
    f.close()
print(you())
'''

#WRITE A PYTHON FUNCTION THAT DISPLAY ALL THE WORDS CONTAING "@cmail" FROM
#THE TEXT FILE "Email.txt"

'''
def mail():
    f=open("Email.txt","r")
    for i in f.read().split():
        if "@cmail" in i :
            print(i)
    f.close()
print(mail())
'''

#WRITE A PY FUNCTION THAT FINDS AND DISPLAY ALL THE WORDS LONGER THAN 5 CHR
#FORM A TEXT FILE "words.txt"

'''
def count():
    f=open("words.txt","r")
    for i in f.read().split():
        if len(i) > 5 :
            print(i)
    f.close()
print(count())
'''

#READ ALL THE RECORDS (USING EXCEPTION HANDLING)

'''
import pickle as pk
f=open("my_file.dat","rb")
while True :
    try:
        print(pk.load(f))
    except EOFError :
        print("END OF FILE !!")
        break
f.close()
'''

##SURYA IS A MANAGER WORKING IN A RECRUITMENT AGENCY. HE NEEDS TO MANAGE
##THE RECORDS OF VARIOUS CANDIDATES. FOR THIS, HE WANTS THE FOLLOWING
##INFORMATION OF EACH CANDIDATE TO BE STORED

##- CANDIDATE_ID – INTEGER
##- CANDIDATE_NAME – STRING
##- DESIGNATION – STRING
##- EXPERIENCE – FLOAT

##YOU, AS A PROGRAMMER OF THE COMPANY, HAVE BEEN ASSIGNED TO DO THIS JOB
##FOR SURYA.

##(I) WRITE A FUNCTION TO INPUT THE DATA OF A CANDIDATE AND APPEND IT IN A
##BINARY FILE.

'''
import pickle as pk
print("DATA WILL SAVE IN THIS FORMATE :")
print("{candidate_ID:[candidate_name , designation , experience ]}")
def recruitment():
    candidate_ID = int(input("candidate_ID : "))
    candidate_name =input("candidate_name :")
    designation =input("designation :")
    experience =int(input("experience in years : "))
    f=open("RECRUITMENT AGENCY.dat","ab")
    data = {candidate_ID:[candidate_name , designation , experience ]}
    pk.dump(data,f)
print(recruitment())
'''

##WRITE A FUNCTION TO UPDATE THE DATA OF CANDIDATES WHOSE EXPERIENCE IS
##MORE THAN 10 YEARS AND CHANGE THEIR DESIGNATION TO SENIOR MANAGER

'''
import pickle as pk
def recruitment():
    f=open("RECRUITMENT AGENCY.dat","rb+")
    r=pk.load(f)
    for i in r :
        try:
            if r[i][2]>10:
                r[i].insert(2,"senior manager")
                r[i].pop(1)
                print(r)
        except EOFError :
            print("FILE END'S HERE !!")
recruitment()
'''

##(III) WRITE A FUNCTION TO READ THE DATA FROM THE BINARY FILE AND DISPLAY THE
##DATA OF ALL THOSE CANDIDATES WHO ARE NOT "SENIOR MANAGER".

'''
import pickle as pk
def recruitment():
    f=open("RECRUITMENT AGENCY.dat","rb+")
    r=pk.load(f)
    for i in r :
        try:
            if r[i][1] != "senior manager" :
                print(r)
        except EOFError :
            print("FILE END'S HERE !!")
recruitment()
'''