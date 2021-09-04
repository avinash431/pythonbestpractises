def Fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a, b
        a, b = b, a+b


for num in Fibonacci(7):
    print(num)