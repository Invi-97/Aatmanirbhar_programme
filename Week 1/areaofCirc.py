#Program 5:- To find the area of the circle 
def area(rad):
    ans = 3.14*(rad)**2
    return ans 

while True:
    r = float(input("Enter the radius :"))
    print("The area of the circle is ",area(r))
    a = input("Do you want to continue (Press Y to continue )")
    if( a == "y" or a =="Y"):
        continue
    else:
        break

# ******OUTPUT******
# Enter the radius :5
# The area of the circle is  78.5
# Do you want to continue (Press Y to continue )
