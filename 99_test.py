
i=1
while i<=5:
    print(i)
    i+=1


num=int(input("enter the number: "))

i=1
while i<=10:
    print(i,".",i*num)
    i+=1


i=10
while i>=1:
    print(i)
    i-=1


fib=[1,4,9,16,25,36,49,64,81,100]

i=0
while i<len(fib):
    print(fib[i])
    i+=1

fib=[1,4,9,16,25,36,49,64,81,100]

num1=16
i=0
while i<len(fib):
    if num1==fib[i]:
        print("found at index: ",i)
    i+=1

