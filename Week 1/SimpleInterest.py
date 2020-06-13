#Program 3 :- To calculate the simple interest

def SimpleIntr(x,y,z):
    print("The Principal amount is :",x," Rupee(s)")
    print("The Rate of Interest is :",y,"%")
    print("The Time period  is :", z,"years")
    return ((x*y*z)/100)

def inp():
    a=float(input("Enter the Principal amount (In Rupees): "))
    b=float(input("Enter the Rate of Interest (In percentage): "))
    c=float(input("Enter the Time Period (In years): "))
    print("The Simple Interest is ", SimpleIntr(a,b,c))

while True:
    inp()
    w = input("Do you want to calculate again ? (Press Y to continue)")
    if(w =='y' or w =='Y') is True:
        continue
    else:
        break

# *********OUTPUT********
# Enter the Principal amount (In Rupees): 4000
# Enter the Rate of Interest (In percentage): 5
# Enter the Time Period (In years): 3
# The Principal amount is : 4000.0  Rupee(s)
# The Rate of Interest is : 5.0 %
# The Time period  is : 3.0 years
# The Simple Interest is  600.0
# Do you want to calculate again ? (Press Y to continue)


