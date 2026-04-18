# n=int(input())
# numb=map(int,input().split())
# squares=map(lambda x:x**2,numb)
# result=sum(squares)
# print(result)


# n=int(input())
# numb=list(map(int,input().split()))
# even=filter(lambda x:x%2==0,numb)
# count=len(list(even))
# print(count)

# n=int(input())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))

# dotprod=sum(x*y for x,y in zip(a,b))
# print(dotprod)

# n=input()
# vowels="aeiouAEIOU"
# if any(c in vowels for c in n):
#     print("Yes")
# else:
#     print("No")

# n=int(input())
# numb=list(map(int,input().split()))
# if all(x>=0 for x in numb):
#     print("Yes")
# else:
#     print("No")

# n=int(input())
# s=input().split()
# long=max(s,key=len)
# print(long)

# n=int(input())
# s=list(map(int,input().split()))
# uniq=sorted(set(s))
# print(*uniq)

# def squaregen(n):
#     for i in range(1,n+1):
#         yield i*i
# n=int(input())
# for s in squaregen(n):
#     print(s)

# def divisby3and4(n):
#     for i in range(0,n+1):
#         if i%3==0 and i%4==0:
#             yield i
# n=int(input())
# for s in divisby3and4(n):
#     print(s,end = " ")

# def squarerange(a,b):
#     for i in range(a,b+1):
#         yield i*i
# a,b=map(int,input().split())
# for s in squarerange(a,b):
#     print(s)

# def countdown(n):
#     while n>=0:
#         yield n
#         n-=1
# n=int(input())
# for s in countdown(n):
#     print(s)

# def fibo(n):
#     a,b=0,1
#     for _ in range(n):
#         yield a
#         a,b=b,a+b
# n=int(input())
# res=list(fibo(n))
# print(",".join(map(str,res)))

# def prime_generator(n):
#     for num in range(2, n + 1):   # check from 2 up to n
#         is_prime = True
        
#         for i in range(2, num):
#             if num % i == 0:      # if divisible, not prime
#                 is_prime = False
#                 break
        
#         if is_prime:
#             yield num             # generator gives prime number


# # Input
# n = int(input())

# # Print primes
# for prime in prime_generator(n):
#     print(prime, end=" ")

# def pwof2(n):
#     for i in range(n+1):
#         yield 2**i
# n=int(input())
# for s in pwof2(n):
#     print(s,end=" ")

# def cycllst(lst,n):
#     for _ in range(n):
#         for item in lst:
#             yield item
# numb=input().split()
# n=int(input())
# for s in cycllst(numb,n):
#     print(s,end=" ")

# import re

# # Read input string
# s = input()

# # Check if the string starts with "Hello"
# match = re.match(r"hi", s)

# # Print result
# if match:
#     print("Yes")
# else:
#     print("No")
    
# import re
# s=input()
# match =re.match(r"hi",s)
# if match:
#     print("yes")
# else:
#     print("no")

# import re
# s=input()
# sub=input()
# search=re.search(sub,s)
# if search:
#     print("yes")
# else:
#     print("no")

# import re
# s=input()
# sub=input()
# findall=re.findall(sub,s)
# print(len(findall))

# from datetime import datetime,timedelta
# dateinput=input()
# days=int(input())
# date=datetime.strptime(dateinput,"%Y.%m.%d")
# newdate=date+timedelta(days=days)
# print(newdate.strftime("%Y.%m.%d"))

# import math
# rise,run=map(int,input().split())
# anglerad=math.atan(rise/run)
# angledegrees=math.degrees(anglerad)
# print(angledegrees)

# import math
# x1,y1,x2,y2=map(int,input().split())
# d=math.sqrt((x2-x1)**2 +(y2-y1)**2)
# print(d)

# from datetime import datetime
# d1 = input()
# d2 = input()
# date1 = datetime.strptime(d1, "%Y-%m-%d")
# date2 = datetime.strptime(d2, "%Y-%m-%d")
# difference = date2 - date1
# print(difference.days)

# import re
# s=input()
# digits=re.findall(r"\d",s)#len digits 
# print(len(digits))

# import re
# s=input()
# match=re.search(r"\S+@\S+\.\S+",s)#Найти первый email в строке.
# if match:
#     print(match.group())

# import json
# data = json.loads(input())
# for user in data:
#     if user["age"] > 18:
#         print(user["name"])

# from datetime import datetime
# dt1 = datetime.strptime(input(), "%Y-%m-%d %H:%M")
# dt2 = datetime.strptime(input(), "%Y-%m-%d %H:%M")
# diff = dt2 - dt1
# minutes = diff.total_seconds() // 60
# print(int(minutes))

# import math
# a,b,c=map(float,input().split())
# d=b**2-4*a*c
# if d>=0:
#     x1=((-b+math.sqrt(d))/2*a)
#     x2=((-b-math.sqrt(d))/2*a)
#     print(x1,x2)

# from datetime import datetime, timedelta

# date = datetime.strptime(input(), "%Y-%m-%d")
# n = int(input())

# new_date = date + timedelta(days=n)

# print(new_date.strftime("%Y-%m-%d"))

# from datetime import datetime,timedelta
# d1=datetime.strptime(input(),"%Y-%m-%d")
# d2=datetime.strptime(input(),"%Y-%m-%d")
# diff=d2-d1
# print(diff.days)
 
print(True or False)