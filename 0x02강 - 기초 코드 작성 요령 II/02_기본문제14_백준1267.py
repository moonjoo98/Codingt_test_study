# 동호는 새악대로 T 통신사의 새 핸드폰 옴머나를 샀다. 새악대로 T 통신사는 동호에게 다음 두 가지 요금제 중 하나를 선택하라고 했다.

# 영식 요금제
# 민식 요금제
# 영식 요금제는 30초마다 10원씩 청구된다. 이 말은 만약 29초 또는 그 보다 적은 시간 통화를 했으면 10원이 청구된다. 만약 30초부터 59초 사이로 통화를 했으면 20원이 청구된다.

# 민식 요금제는 60초마다 15원씩 청구된다. 이 말은 만약 59초 또는 그 보다 적은 시간 통화를 했으면 15원이 청구된다. 만약 60초부터 119초 사이로 통화를 했으면 30원이 청구된다.

# 동호가 저번 달에 새악대로 T 통신사를 이용할 때 통화 시간 목록이 주어지면 어느 요금제를 사용 하는 것이 저렴한지 출력하는 프로그램을 작성하시오.

# My solution 1
import sys
a = int(sys.stdin.readline().strip())

b_list=list(map(int,sys.stdin.readline().split()))

y=0
m=0


for j in range(a):
    y_a,y_b=divmod(b_list[j],30)
    m_a,m_b=divmod(b_list[j],60)

    y_b = 1
    m_b = 1  
    

    if b_list[j] < 30 :
        y+=10; m+=15
    elif 30<= b_list[j] < 60:
        y+=20; m+=15
    else:
        y+= (y_a*10) + ( y_b* 10)
        m+= (m_a*15) + ( m_b* 15)
    
if y == m :
    print(f'Y M {y}')
elif y < m :
    print(f'Y {y}')
else:
    print(f'M {m}')

# solution 2
import sys
a = int(sys.stdin.readline().strip())

b_list=list(map(int,sys.stdin.readline().split()))

y=0
m=0

for j in range(a):
    y+=((b_list[j]//30) + 1 )* 10
    m+=((b_list[j]//60) + 1 )* 15    
if y == m :
    print(f'Y M {y}')
elif y < m :
    print(f'Y {y}')
else:
    print(f'M {m}')
