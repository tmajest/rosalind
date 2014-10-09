# http://rosalind.info/problems/fib/
# iterative solution

# f(n) = f(n-1) + k*f(n-2)
def rabbits(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, (a * k) + b

    return b

n, k = map(int, raw_input().split(" "))
print rabbits(n, k)
