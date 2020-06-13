# Write a python function to check whether the given number is prime or not??
def prime():
    number = int(input("Enter any number: "))
    if number == 1:
        print("1 is neither Prime nor Composite number")
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
    
prime()

# **********OUTPUT*********
# Enter any number: 10
# 10 is not a prime number