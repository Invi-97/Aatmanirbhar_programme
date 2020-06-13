# Program 3:- A permutation of a list is another list with the same elements, but in a possibly different order.
# Example: [1, 2, 1] is a permutation of [2, 1, 1], but not of [1, 2, 2]. 
# Write a function is permutation (list1, list2): bool that returns True if its Arguments are permutations of each other.
L1 = [1,2,1]
L2 = [2,1,1]

def isPermutation(list1,list2):
 if len(list1) != len(list2):
   return False
 for i in range(0, len(list1)):
   if list1.count(list1[i]) != list2.count(list1[i]):
     return False

def is_list_permutation(list1,list2):
  if (isPermutation(list1,list2) == False): 
    return False 
  elif not list1:
    print("they are not the permutations of each other")
  else:
    print("they are permutations of each other")

print("The lists are ",L1,L2)
print(is_list_permutation(L1,L2))

# ********OUTPUT**********
# The lists are  [1, 2, 1] [2, 1, 1]
# they are permutations of each other