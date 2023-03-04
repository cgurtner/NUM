# Fibonacci ohne Rekursion
def fibo_for(n):
    res = [0, 1]
    for i in range(2, n+1):
        res.append(res[i-1] + res[i-2])
    return res[n]

print(fibo_for(8))
