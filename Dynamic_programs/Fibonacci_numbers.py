def fibonacciByRecurse(n):
    if n<=1:
        return n
    else:
        return fibonacciByRecurse(n-1)+fibonacciByRecurse(n-2)

print(fibonacciByRecurse(10))