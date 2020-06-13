#Program 2 :- To print all the Prime numbers in an given interval

lower = int(input("Enter a starting number"))
upper = int(input("Enter a ending number "))

print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# ******OUTPUT******
# Enter a starting number100
# Enter a ending number 200
# Prime numbers between 100 and 200 are:
# 101
# 103
# 107
# 109
# 113
# 127
# 131
# 137
# 139
# 149
# 151
# 157
# 163
# 167
# 173
# 179
# 181
# 191
# 193
# 197
# 199