def fibo(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b = b,a+b
n=int(input())
result =list(fibo(n))
print(",".join(map(str,result)))


# def even_numbers(n):
#     for i in range(0, n + 1):
#         if i%3==0 and i%4==0:
#             yield i

# n = int(input())

# print(" ".join(map(str, even_numbers(n))))