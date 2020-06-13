#Program 1:- Addition of 2 numbers 
def add(x,y):
    print("The addition is : ")
    return x+y

while True:
    print(add(int(input("Enter 1st number: ")),int(input("Enter 2nd number: "))))
    a=input("Do you want to continue (Press Y to continue)")
    if(a=='y' or a=='Y') is True:
        continue
    else:
        break
        

#***********Output**********
# Enter 1st number: 45
# Enter 2nd number: 55 
# The addition is : 
# 100
# Do you want to continue (Press Y to continue)y
# Enter 1st number: 

