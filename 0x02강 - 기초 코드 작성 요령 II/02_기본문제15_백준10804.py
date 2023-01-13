
#My solution 1 
import sys

card_=list(range(0,21))

for _ in range(10):
    a,b = map(int,sys.stdin.readline().split())
    
    for i in range((b-a+1)//2):
        temp= card_[b-i]
        card_[b-i]=card_[a+i]
        card_[a+i]=temp

card_.pop(0)

for i in card_:
    print(i,end=' ')

