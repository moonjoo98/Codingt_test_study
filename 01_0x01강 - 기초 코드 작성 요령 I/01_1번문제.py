
def multi_sum(x):
    cnt=0
    for i in range(x+1):
        if (i % 3 == 0 or i % 5 == 0):
            cnt += i
            
    return cnt

print(multi_sum(34567))