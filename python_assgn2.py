# -------------task3-------------
# Q1
'''
lst10Elem = [7, 'String', 2 + 3j, 3.7]'''
# print(lst10Elem)

# --------------------------

# Q2
'''
py_list = [7, 77, 777, 7777, 7777]
print("The length of list is", len(py_list,), "and the sliced values are", py_list[1:3])'''

# ----------------------------
# Q3
'''
from math import prod
lst = [2,4,6,8,10]
print(sum(lst))
print(prod(lst)) '''
# -------------------------

# Q4
'''
from random import randrange
x=[]
for i in range(10,100):
    x.append(i)
print("The appended list is: ",x)
print("The largest number of the list is: ", max(x))
print("The smallest number of the list is: ", min(x))'''
# -------------------------

# Q5
'''
lst1 = []
for i in list(range(50, 100)):
    if i % 2 != 0:
        lst1.append(i)
        True
print(lst1)'''
# -----------------------------

# Q6
'''
sqrLst = list()
for i in range(1,30):
    sqrLst.append(i ** 2)
print(sqrLst[:5]+sqrLst[-5:])'''
# ----------------------------

# Q7
'''
tstlst = [1,3,5,7,9,10]
nwlst=[2,4,6,8]
tstlst.pop()
tstlst.extend(nwlst)
print(tstlst)'''
# -----------------------

# Q8
'''
dict1={1:10,2:20}
dict2={3:30,4:40}
contdict={}
for i in (dict1,dict2):
    contdict.update(i)
print(contdict)'''
# ---------------------

# Q9
'''
val = int(input("Enter a value: "))
sqrdict= {}
for i in range(1, val+1):
    sqrdict[i]=i*i
print(sqrdict)'''
# ------------------------

# Q10
'''
UsIn= (input("Enter some comma-separated values: "))
lst = UsIn.split(",")
tup = tuple(lst)
print("List is: ", lst)
print("Tuple is: ", tup)'''
# -------------------------

## ---------------------------------------Task4-------------------------------

# Q1
'''
rvstr = input("Enter a string: ")
print(rvstr[::-1])'''


# ----------------------------

# Q2
'''
def str_test(sentence):
    str_dict = {"UpperCase": 0, "LowerCase": 0}
    for i in sentence:
        if i.isupper():
            str_dict["UpperCase"] += 1
        elif i.islower():
            str_dict["LowerCase"] += 1
        else:
            pass
    print("Sentence is: ", sentence)
    print("No. of Uppercase characters", str_dict["UpperCase"])
    print("No. of Lowercase characters", str_dict["LowerCase"])


str_test("abcSdefPghijQkL")'''
# --------------------------------------
