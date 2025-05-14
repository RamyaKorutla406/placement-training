'''def fun(n):
    if n==0:
        return
    print(n,end=" ")
    fun(n-1)
n=5
fun(n)'''# 5 4 3 2 1

'''def fun(n):
    if n==0:
        return
    print(n,end=" ")
    fun(n-1)
n=5
fun(n)'''#1 2 3 4 5
#..
'''def fun(n):
    if n==0:
        return 200
    result=fun(n-1)
    print(n,end=" ")
    return result
n=5
print(fun(n))'''
#...
#5 4 3 2 1 1 2 3 4 5
'''def fun(n):
    if n==0:
        return
    print(n,end=" ")
    fun(n-1)
    print(n,end=" ")
n = int(input())
(fun(n))'''

#5 4 3 2 1 2 3 4 5 
'''def fun(n):
    if n==0:
        return
    print(n,end=" ")
    fun(n-1)
    if n!=1:
        print(n,end=" ")
n = int(input())
(fun(n))'''
#odd numbers
'''def fun(n):
    if n==0:
        return
    if n%2!=0:
       print(n,end=" ")
    fun(n-1)
    if n%2!=0:
        print(n,end=" ")
n = int(input())
(fun(n))'''
#1 2 3 4 5 5 4 3 2 1
'''def fun(n,m=0):
    if n==m:
        return
    print(m+1,end=" ")
    fun(n,m+1)
    print(m+1,end=" ")
n=5
fun(n)'''
#.natural numbers
'''n = int(input())
if n < 1:
    print("Please enter a natural number (greater than 0).")
else:
    print("Natural numbers:")
    for i in range(1, n + 1):
        print(i)'''
#odd number
'''def fun(n):
    if n==0:
        return
    fun(n-1)
    if n%2!=0:
       print(n,end=" ")
n = int(input())
(fun(n))'''
#.even numbers
'''def fun(n):
    if n==0:
        return
    fun(n-1) 
    if n%2==0:
        print(n,end=" ")
n = int(input())
(fun(n))'''
#.factorial
'''n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)'''
#fibanocci series
'''n = int(input())
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b'''
#.prime number
'''n=int(input())
flag=0
for i in range(2,int(n**(1/2))+1):
    if n%i==0:
        flag+=1
        break
if flag==0:
    print("prime")
else:
    print("not prime")'''
#prime number using recursion
'''def is_prime(n,i=2):
    if i*i>n:
        return True
    if n%i==0:
        return False
    return is_prime(n,i+1)
n=int(input())
if is_prime(n):
    print("prime number")
else:
    print("not prime number")'''
#min steps
'''def fun(n):
    if n==1:
        return 0
    elif n%2==0:
        return 1+fun(n//2)
    else:
        return 1+min(fun(n-1),fun(n+1))
n=15
print(fun(n))'''
#sum of numbers in list using recursion
'''def fun(l,i=0):
    if i==len(l):
        return 0
    return l[i]+fun(l,i+1)
l=[1,4,3,2,5]
print(fun(l))'''
#count of prime numbers
def fun(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def count(num):
    if not num:
        return 0
    if fun(num[0]):
        return 1 + count(num[1:])
    else:
        return count(num[1:])
n=list(map(int, input().split()))
print(count(n))
