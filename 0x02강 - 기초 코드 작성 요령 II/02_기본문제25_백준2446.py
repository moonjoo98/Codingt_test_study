import sys
n=int(sys.stdin.readline().strip())

for i in reversed(range(1,n+1)):
    print(" "*(n-i)+"*"*(2*i-1),sep='\n')    
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1),sep='\n')
