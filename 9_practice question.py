#WAP to find the sum of first n natural numbers (using while)
n=int(input("enter the no: "))
i=0
sum=0
while i<=n:
    print(i)
    sum=sum+i
    i+=1
print("total sum: ",sum)


#WAP to find the sum of first n natural numbers (using for in range)
n=int(input("enter the no: "))
sum=0
for i in range (n+1):
    print(i)
    sum=sum+i
print("total sum: ",sum)

#WAP to find factorial of first n numbers (using for)
n=int(input("enter the no: "))
fact=1
i=0
for i in range (1,n+1):
    print(i)
    fact=fact*i

print("factorial is: ",fact)


#WAP to find factorial of first n numbers (using while)
n=int(input("enter the no: "))
fact=1
i=1
while i<=n :
    print(i)
    fact=fact*i
    i+=1
print("factorial is: ",fact)


