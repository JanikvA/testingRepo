def fib(n: int) -> int:
    for i in range(1, 2):
        print("hello")
        x = 4
        print(x)
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
