#print no. from 1to 100
i=1
while i<=100:
    print(i)
    i+=1


#print number from 100 to 1
j=100
while j>=1:
    print(j)
    j=j-1

#print the multiplication table of a number

num=int(input("enter the number: "))
i=1
while i<=10:
    print(i*num)
    i=i+1

"""
print the elements of the following list using loop
[1,4,9,16,25,36,49,64,81,100]
"""
nums=[1,4,9,16,25,36,49,64,81,100]
k=0
while k<len(nums):
    print(nums[k])
    k=k+1



"""
search for a number X in this tuple using loop
[1,4,9,16,25,36,49,64,81,100]
"""

print("1,4,9,16,25,36,49,64,81,100")


x=int(input("enter the number from the following: "))
nums=(1,4,9,16,25,36,49,64,81,100)
i=0
while i<len(nums):
    if nums[i]==x:
        print("found at index: ",i)
    else:
        print("finding at index ... ",i)
    i=i+1



