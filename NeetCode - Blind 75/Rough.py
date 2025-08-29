def primeFactor():
    primeFactor = []
    n = 56
    i = 2
    while i * i <= n:
        if n % i == 0:
            primeFactor.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        primeFactor.append(n)
    return (primeFactor)

print(primeFactor())