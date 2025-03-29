i=0
while i<=10:
    print(i)
    if i==5:
        break
    i+=1
print("end of loop")

print("****************************************************")
fib=[1,4,9,16,25,36,49,64,81,100]

num1=16
i=0
while i<len(fib):
    if num1==fib[i]:
        print("found at index: ",i)
        break
    else:
        print("finding at index: ",i)
    i+=1

print("****************************************************")

i=0
while i<=5:
    if i==3:
        print("found")
        i+=1
        continue
    print(i)
    i+=1
print("****************************************************")


fib=[1,4,9,16,25,36,49,64,81,100]

num1=16
i=0
while i<len(fib):
    if num1==fib[i]:
        print("found at index: ",i)
        i+=1
        continue #acts as skip
    print("finding at index: ",i)
    i+=1
print("****************************************************")

i=0
while i<=10:
    if i%2==0:
        print(i)
    i=i+1


print("****************************************************")
i=0
while i<=10:
    if i%2==0:
        i+=1
        continue
    print(i)
    i=i+1
print("****************************************************")



i=0
while i<=10:
    if i%2!=0:
        print(i)
    i=i+1
print("****************************************************")

i=0
while i<=10:
    if i%2!=0:
        i+=1
        continue
    print(i)
    i=i+1
