# 다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

# 다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

#my solution 1
import sys
arr = [0]*10

a = sys.stdin.readline().strip()

for i in a :
    arr[int(i)]+=1


for i in range(1000000):
    if arr[6] < arr[9]:
        arr[6] +=1
        arr[9] -=1
    elif arr[6] > arr[9]:
        arr[6] -= 1
        arr[9] += 1
    else:
        break
    
        

print(max(arr))
    
#solution 2
n = input() #다솜이 방번호를 string으로
card=[0]*10 #0~9까지 번호
card_6n9 = 0

for i in n:
    if(i=='6' or i=='9'): #6,9 동일취급
        card_6n9 += 1
    else:
        card[int(i)] += 1

#6, 9 개수 결정
if(card_6n9 % 2 == 0):
    card_6n9 = card_6n9//2
else:
    card_6n9 = card_6n9//2 + 1

card[6] = card_6n9

#card에 있는 것들 중 최대값이 세트의 개수
print(max(card))