
def isPrime(N):
        if N == 1:
            return False     
        i = 2
        while i*i <= N:
            if N % i == 0:
                return False
                
            i += 1
                
        return True

def isPrimeFactor(n):
    res = []
    for i in range(2, n+1):
        if  isPrime(i):
            x = i
            while n%x == 0:
                res.append(i)
                n = n / i
    return res

print(isPrimeFactor(100))

