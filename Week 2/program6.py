# Write a python program that prints all the numbers from
# 0 to 6 except 3 and 6?
# Note: use ‘continue ‘statement.
# Expected output: 0 1 2 4 5

for x in range(7):
    if x == 6 or x == 3:
        continue
    else:
        print(x)
    
# ********OUTPUT*********
# 0
# 1
# 2
# 4
# 5

