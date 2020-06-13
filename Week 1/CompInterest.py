# Program 4:- To find the compound interest 
def compIntr(prin, rate, time):
    result = prin*(pow((1+ rate/100),time))
    return result

while True:
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the rate of interest: "))
    t = float(input("Enter the time in years:"))

    amount =compIntr(p,r,t)
    interest = amount - p
    print("Compound amount is %2.f" %amount)
    print("Compound Interest is %2.f" %interest)
    a = input("Do you want to calculate more? (Press Y to continue)")
    if(a=="Y" or a=="y"):
        continue
    else:
        break

# *********OUTPUT**********
# Enter the principal amount: 4000
# Enter the rate of interest: 4
# Enter the time in years:3
# Compound amount is 4499
# Compound Interest is 499
# Do you want to calculate more? (Press Y to continue)

    
