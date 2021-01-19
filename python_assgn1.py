# --------------------------------TASKONE--------------------
"q1"

'''var1, var2, var3 = 100, 10.01, str(100)
print(type(var1), type(var2), type(var3))
'''

# -----------------------------------------
"q2"
'''comp = 1 + 2j
print(comp, "is of type", type(comp))

swap = 999
print(comp, "is  now of type", type(swap))

comp = swap
print("complex data type swapped to", type(comp))'''

# ----------------------------------------------

"q3"

"using third variable"
'''
num1 = 10
num2 = 20

temp = num1
num1 = num2
num2 = temp

print('The value of num1 after swapping: {}'.format(num1))
print('The value of num2 after swapping: {}'.format(num2))

"without using third variable"

ab = 5
cd = 25

ab,cd = cd,ab
print("value of ab is", ab, "after swapping", "and", "value of cd is", cd, "after swapping")'''

# --------------------------------------------------------------
"q4"
'''
inp1 = input("enter a number: ")
print(inp1)'''

# -------------------------------------------------------
"q5"

import random
from random import randrange

'''
a = int(input("enter a number between 1 and 10: "))
b = int(input("enter another number between 1 and 10:"))

if 1 <= (a and b) <= 10:
    z = a + b
    z += 30
    res = z
    print("your result is", res)
else:
    print(" given input is not in range")'''

# -------------------------------------------------------

"q6"

'''
fltype = 10.10
int1 = 100
str1 = "it's a string data type"


print("The data type of", fltype, "is", type(fltype),"\n", "The data type of", int1, "is", type(int1), "\n",
      "The data type of", str1, "is", type(str1))'''
# -------------------------------------------------------
"q7"
'''
varCase = "lowerCamel"
VarCase = "UpperCamel"
var_case = "snake_case"
VARCAS = "constant"
print(varCase, "is lower camel variable format", "\n", VarCase, "is upper camel variable format", "\n",
     var_case, "is snake case variable format", "\n", VARCAS, "is upper case variable format and ususlly contains constant value")'''
# -------------------------------------------------------

"q8"
'''dumvar = 50179028
dumvar = "it's now a string data type"

print(dumvar)'''
'''Variables are essentially like an empty box, that can contain something like a string, number, or other value.
When you assign it a value, the box will contain that value, and when you reassign it, it will overwrite the old value,
and the new value will be placed inside of it.'''
# ------------------------------------------------------------

# TASKTWO

"Q1"
'''
oper = [6,25, 15]
for i in oper:
    if i%3==0:
        print("consultadd")
    elif i%5==0:
        print("Python Training")
    elif i%3 ==0 and i%5 ==0:
        print("consultadd-python training")
    else:
        print("try something else")'''
# ----------------------------------------------------
"Q2"
'''
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
oper = input("Choose the operation to perform specific operation 1 is Add,2 is sub,3 is Mult,4 is div,5 is Avg: ")

num3 = int(input("Enter First Number to cal avg using option 5: "))
num4 = int(input("Enter second Number to cal avg using option 5: "))

result = 0
if oper == '1':
    result = num1+num2
    print("Addition")
elif oper == '2':
    result = num1-num2
    print("Subtraction")
elif oper == '3':
    result = num1*num2
    print("Multiplication")
elif oper == '4':
    result = num1/num2
    print("Division")
elif oper =='5':
    result = (num1+num2)/2
    print("Average")
else:
    print("Input character is not recognized!")

print("Your output is", ":", result)

if result < 0:
    print("Negative")'''

# -------------------------------------------------------------
"Q3"
'''
a=10
b=20
c=30
avg = (a+b+c)/3
print("avg = ",avg)
if avg > a and avg > b and avg > c:
    print("avg is higher than a, b, and c")
elif avg > a and avg > b:
    print("avg is higher than a, b, and c")
elif avg > a and avg > c:
    print("avg is higher than a and c")
elif avg > b and avg > c:
    print ("avg is higher than b and c")
elif avg >a:
    print("avg is just higher than a")
elif avg > b:
    print("avg is just higher than b")
elif avg > c:
    print("avg is just higher than c")
else:
    print("something is wrong")
print("you have successfully implemented the given flowchart")'''

# -------------------------------------------------------------
"Q4"
"(i)"
'''
av=0
UserInput = int(input("Enter a number: "))
num=0
while num<=UserInput:
    if num<av:
        break
    print("working")
    num+=1
print("it's over")'''

"(ii)"
'''
UsIn = int(input("Enter a number: "))
val=0
while val > UsIn:
    continue
print("going good")'''

# --------------------------------------------------------

"Q5"
'''
for i in range(2000,3000):
    if i%7==0 and i%5!=0:
        print(i)'''
# -------------------------------------------
"Q6"
"(i)"
'''
x= 123
for i in x:
    print(i)'''
# 'int' object is not iterable

"(ii)"
'''
i=0
while i<5:
    print(i)
    i+=1
    if i==3:
        break
    else:
        print('error')'''

"(iii)"
'''
count=0
while True:
    print(count)
    count+=1
    if count>=5:
        break'''
# ---------------------------------------------
"Q7"
'''
for i in range(0,6):
    if i==3:
        continue
    print(i, end ="\n")'''
# -------------------------------------------
"Q8"
'''
value = input("Insert a string input: ")
inp1=0
inp2=0

for i in value:
    if i.isalpha():
        inp1 = inp1+1
    elif i.isdigit():
        inp2 = inp2+1
    else:
        pass
print("Letters", inp1)
print("Digits", inp2)'''
# ------------------------------------------------

"Q9"
"(i)"
'''
val = 7
UserInp = eval(input("Guess a number: "))
while UserInp>0:
    if val!=UserInp:
        print("not right")
        UserInp = eval(input("Guess a number: "))
    else:
        print("you got it")
        break'''

"(ii)"
'''
val = 7
UserInp = eval(input("Guess a number: "))
while UserInp>0:
    if val!=UserInp:
        print("not a right guess")
        answer=input('do you want to continue?: Yes/No ')
        if answer=="Yes":
            UserInp = eval((input("Guess a number: ")))
        else:
            print("Thank you")
            break
    else:
        print("you got it")
        break'''
# --------------------------------------------
"Q10"
"(i)"
