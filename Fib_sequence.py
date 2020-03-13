def fib_sequence(n):

    if n<= 1:
        return n
    else:
        return(fib_sequence(n-1)+ fib_sequence(n-2))
nterms = 25


if nterms <= 0:
    print("Enter a postive integer.")
else:
    print("Fibonacci Sequence:")
    for i in range(nterms):
        print(fib_sequence(i))
