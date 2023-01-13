import sys


list_=[]
for i in range(9):
    a=int(sys.stdin.readline().strip())
    list_.append(a)
max_=max(list_)
print(max_)
print(list_.index(max_)+1)
