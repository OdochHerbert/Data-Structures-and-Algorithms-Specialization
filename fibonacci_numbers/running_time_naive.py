#FINDING RELATIONSHIP BTN fib_recurs() and rtime()
def rtime(n):
    if n<=1:
        return 2
    else:
        return rtime(n-1) + rtime(n-2) + 3

print(rtime(20))