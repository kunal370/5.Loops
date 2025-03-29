'''
using for
print the elements of the following list using loop:
[1,4,9,16,25,36,49,64,81,100]
'''

list1=[1,4,9,16,25,36,49,64,81,100]
for i in list1:
    print(i)

'''
search the number in this tuple using loop
[1,4,9,16,25,36,49,64,81,100]
'''
indx=0
tup1=(1,4,9,16,25,36,49,64,81,100)
X=int(input("enter the number: "))
for i in tup1:
    if i==X:
        print(i,"--> no. found at index: ",indx)
        continue
    indx+=1
    print(i)
