# def fib(n):
#     if n <= 1:
#         return 1
#
#     return fib(n-1) + fib(n-2)
#
# print (fib(8))

def fibonacci(n):

    if n == 0:
        return []
    elif n == 1:
        return [1]

    seq = [0] * n
    seq[0], seq[1] = 1, 1

    for i in range(2, n):
        seq[i] = seq[i-1] + seq[i-2]

    return seq

print(fibonacci(0))