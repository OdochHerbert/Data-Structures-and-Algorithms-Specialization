import numpy as np;
def fin_eff(n):
    numbers = np.empty(n+1)
    numbers[0]=0
    numbers[1]=1
    for i in range(2,n+1):
        numbers[i]=numbers[i-1]+numbers[i-2]
    return numbers[n]
print('finnobacci is ',fin_eff(20))

#running_time
def run_time(n):
    time = (2*n)+2
    return time
print('time is ', run_time(20))