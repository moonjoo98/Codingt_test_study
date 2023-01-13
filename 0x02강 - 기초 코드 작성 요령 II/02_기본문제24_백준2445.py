import sys
n=int(sys.stdin.readline().strip())
for i in range(1,n+1):
    print("*"*i+" "*2*(n-i)+"*"*i,sep='\n')
for i in reversed(range(1,n)):
    print("*"*i+" "*2*(n-i)+"*"*i,sep='\n')    

