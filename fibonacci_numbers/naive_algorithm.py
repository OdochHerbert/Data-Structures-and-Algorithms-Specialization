def fib_recurs(n):
    if (n<=1):
        return n
    else:
        return (fib_recurs(n-1)+fib_recurs(n-2))

print(fib_recurs(20))
