def fibByDp(n,memo={}):
    if n<= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n]=fibByDp(n-1,memo)+fibByDp(n-2,memo)

    return memo[n]

print(fibByDp(10))
