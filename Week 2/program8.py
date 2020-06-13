# Program 8: Write a python function to check whether the given number is Adam number or not

number = input("Enter a number: ")
reverse = number[::-1]
number_sqr = int(number)**2
reverse_sqr = int(reverse )**2
if int(number_sqr ) == int(str(reverse_sqr)[::-1]):
   print(number," is a adam number")
else:
   print(number," is not a adam number")

# *******OUTPUT*******
# Enter a number: 12
# 12  is a adam number