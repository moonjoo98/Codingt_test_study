import sys
s_list= list(sys.stdin.readline().strip())
num_= int(sys.stdin.readline().strip())
c_list=[]

for _ in range(num_):
    ctrl=list(map(str,sys.stdin.readline().split()))
    
    if ctrl[0] == 'P':
        s_list.append(ctrl[1])
    
    elif ctrl[0] == 'L':
        if s_list:
            c_list.append(s_list.pop())
        else:
            continue
    
    elif ctrl[0] == 'D':
        if c_list:
            s_list.append(c_list.pop())
        else:
            continue        
    else :
        if s_list:
            s_list.pop()
        else:
            continue            
print("".join(s_list+list(reversed(c_list))))