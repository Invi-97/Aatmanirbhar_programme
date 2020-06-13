# Write a python program to count the number of even and odd numbers from a series of numbers??
# Sample numbers: numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected output:
# Number of even numbers: 4
# Number of odd numbers: 5

a = int(input("Enter the number of elements you want to enter: "))
l1=[]
for i in range(a):
    b = int(input("Enter the number: "))
    l1.append(b)
print("the numbers are",l1)

eve = 0
odd = 0
for x in l1:
    if x%2 == 0:
        eve += 1
    else:
        odd += 1 

print("Number of even numbers are : ", eve)
print("Number of odd numbers are : ",odd)


# *********OUTPUT*************
# Enter the number of elements you want to enter: 9
# Enter the number: 1
# Enter the number: 2
# Enter the number: 3
# Enter the number: 4
# Enter the number: 5
# Enter the number: 6
# Enter the number: 7
# Enter the number: 8
# Enter the number: 9
# the numbers are [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Number of even numbers are :  4
# Number of odd numbers are :  5