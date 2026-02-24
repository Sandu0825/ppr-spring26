n = int(input())
sum=list(map(int,input().split()))
sm=0
pos=1
for i in range(n):
    if sum[i]%2==0:
        sm+=sum[i]
print(sm)