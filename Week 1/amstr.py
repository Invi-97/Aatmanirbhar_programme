#Program 1 :- To find Amstrong number
num = int(input("Enter a number : "))
ans = 0
temp = num

while temp > 0:
    digit = temp % 10
    ans += digit ** 3
    temp //= 10 

if num == ans:
    print("the number is an amstrong number ")
else:
    print("the number is NOT an amstrong number")

# **************OUTPUT********
# Enter a number : 153
# the number is an amstrong number
