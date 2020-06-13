#Program 1 :- Read two lists from the user. Two lists contain the names of students?? 
# ➢ Get the Names which are there in both lists??
# ➢ Get the Names which are there in atleast one list??
# ➢ Get the Names which are there in List1 not there in List2??
# ➢ Get the names which are there in List2 not there in List1??
l1=[]
a = int(input("Enter the number totlal of student you want in list 1: "))
for x in range(a):
    b = input("Enter the name of the student: ")
    l1.append(b)
print("List 1 :",l1)

l2=[]
a = int(input("Enter the number totlal of student you want in list 2: "))
for x in range(a):
    b = input("Enter the name of the student: ")
    l2.append(b)
print("List 2 :",l2)

l3=[]
for x in l1:
    if x in l2:
        l3.append(x)
print("Common students in both the lists are ",l3)

l4=[]
for y in l1:
    if y not in l2:
        l4.append(y)
print("Students only in list 1 and not in list 2 are :",l4)

l5=[]
for z in l2:
    if z not in l1:
        l5.append(z)
print("Students in list 2 but not in list 1 are :",l5)

l6=[]
for x in l1:
    if not(x in l2):
        l6.append(x)
print("students in either lists are ",l6)

# ***********OUTPUT**********
# Enter the number totlal of student you want in list 1: 4
# Enter the name of the student: yash  
# Enter the name of the student: Harsh
# Enter the name of the student: pranit
# Enter the name of the student: paras
# List 1 : ['yash', 'Harsh', 'pranit', 'paras']
# Enter the number totlal of student you want in list 2: 4
# Enter the name of the student: yash
# Enter the name of the student: paras
# Enter the name of the student: vedant
# Enter the name of the student: raj
# List 2 : ['yash', 'paras', 'vedant', 'raj']
# Common students in both the lists are  ['yash', 'paras'] 
# Students only in list 1 and not in list 2 are : ['Harsh', 'pranit']
# Students in list 2 but not in list 1 are : ['vedant', 'raj']
# students in either lists are  ['Harsh', 'pranit']
