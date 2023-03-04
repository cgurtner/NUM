# Fibonacci ohne Rekursion
def fibo_for(n):
    res = [0, 1]
    for i in range(2, n+1):
        res.append(res[i-1] + res[i-2])
    return res[n]

print(fibo_for(8))

# Fibonacci mit Rekursion
def fibo_rec(n):
    if n <= 1:
        return [0, 1][:n+1]
    else:
        fib = fibo_rec(n-1)
        fib.append(fib[-1] + fib[-2])
        return fib

print(fibo_rec(8))