def power(x):
    cnt = 1
    while 2*cnt <= x:
        cnt *= 2
    return cnt 

print(power(5))
print(power(97615282))
print(power(1024))
