# Write a python function that checks whether a passed string is palindrome or not??

def palindrome(st):
   return st == st[ : :-1]

st = input("Enter a word to check: ")
sol = palindrome(st)

if sol:
    print(st,"is a palindrome")
else:
    print(st,"is not a palindrome")

# ********OUTPUT**********
# Enter a word to check malayalam
# malayalam is a palindrome