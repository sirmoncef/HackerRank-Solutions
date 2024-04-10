
def checkstrict (SET1,NUMBEROFSET):
 for i in range(NUMBEROFSET):
    B = set(map(int,input().split()))
    for j in SET1:
        if (all(j) in B or not(j in B)):
            k = False
        else:
            k = True   

 return k
          
A = set(map(int,input().split()))
N = int(input())


checkstrict(A,N)

