#Program 2 :- Factorial of a number

def fact(num):
    return 1 if (num == 1 or num == 0) else num * fact(num-1)

while True:
    a = int(input("Enter a number : "))
    fact(a)
    print("Factorial of number ",a," is ",fact(a))
    z=input("Do you want to calculate again ? (Press Y to continue)")
    if(z=='y' or z=='Y') is True:
        continue
    else:
        break


# **********OUTPUT**********
# Enter a number : 5
# Factorial of number  5  is  120

# Enter a number : 0
# Factorial of number  0  is  1