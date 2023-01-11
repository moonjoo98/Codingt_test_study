def arr_sum(x,y):
    for i in range(0,y-1):
        for j in range(i+1,y):
            if (x[i] + x[j] == 100) :
                return 1
    return 0 

arr_sum([1,52,48],3)
arr_sum([50,42],2)
arr_sum([4,13,63,87],4)
