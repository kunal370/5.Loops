list=[1,2,3,4,5,6,7,8,9,0]
for i in list:
    if i==7:
        print("found at",list[i])
print("******************************************")
str="kunal"
for i in str:
    print(i)


print("******************************************")
str="kunal"
for i in str:
    if i=="p": # ""<-- depends on if else condition execute or not
        print(i,"found")
        break
    print(i)
else:
    print("end")
print("******************************************")