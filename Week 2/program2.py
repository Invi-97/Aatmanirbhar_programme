# Take a list of Numbers or Names with repetitive values??
# ➢ Get a list as output??
# ➢ Each sublist has the number and how many times it is there in the list??
# ➢ The output should be in sorted order based on count??
# ➢ If the count is equal different numbers .sort them based on numbers??
# Example: [23, 45, 23, 77, 67, 45, 45, 2, 3, 3, 2, 3]
# Output : [ [3,3], [45,3], [2,2], [23,2], [67,1], [77,1] ]

l1=[]
num = int(input("Enter the number of elements you want in the list "))
for x in range(num):
    a = input("Enter the list ( with or without repetition )")
    l1.append(a)
print("The numbers in the list are ",l1)

l2=l1
count = 0
l3={}
for i in range(0,len(l2)):
    for j in range(i + 1,len(l2)):
        if(l2[i]==l2[j]):
            rep = l2[j]
            rep=[]
            print("repeated element is ",l2[j])
            count += 1
            for x in range(count):
                l3={l2[j]:count}
                if 
                    continue
                else:
                    l3.update(l3)
            
print(l3)
            