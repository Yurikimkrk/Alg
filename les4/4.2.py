from timeit import timeit


def sieve(x):
    n = x * 20
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res[x - 1]


print(timeit('sieve(5)', number=100, globals=globals()))  # 0.0036647999999999993
print(timeit('sieve(50)', number=100, globals=globals()))  # 0.0446994
print(timeit('sieve(500)', number=100, globals=globals()))  # 0.4937424


def prime(x):
    global num
    num = 0
    count = 0
    a = 2
    while count < x:
        d = 2
        while a % d != 0:
            d += 1
        if d == a:
            num = a
            count += 1
        a += 1
    return num


print(timeit('prime(5)', number=100, globals=globals()))  # 0.00046880000000000185
print(timeit('prime(50)', number=100, globals=globals()))  # 0.0472382
print(timeit('prime(500)', number=100, globals=globals()))  # 10.6192674

# Сложность реализации решета Эратосфена линейная, собственной реализации с циклами - квадратичная.
# На больших числах эффективнее реализация решета
