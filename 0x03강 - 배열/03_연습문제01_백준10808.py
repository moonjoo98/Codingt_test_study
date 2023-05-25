
#solution 1
import sys 

a = sys.stdin.readline().strip()

result = [0] * 26

for i in a:
    result[ord(i)-ord('a')] +=1
print(*result)

#solution 2
import sys

word = sys.stdin.readline().strip()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
arr = [0] * 26

for i in range(26):
    for j in word:
        if alpha[i]== j :
            arr[i] +=1

print(*arr)