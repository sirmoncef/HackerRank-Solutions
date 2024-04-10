from itertools import permutations 

def perm(string,width):
   if 0 < k < len(string):
      g = permutations(string,k)

      for i in g:
         print(i[0],end="")
         print(i[1])


string0 ,width0 = input().split()

k = int(width0)

perm(sorted(string0),k)


