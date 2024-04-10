l = list(map(int,input().split()))
n = int(input())

for i in range(len(l)):
 for j in range(i,len(l)):
  if (l[i]+l[j] == n):
    print(list([i,j]))