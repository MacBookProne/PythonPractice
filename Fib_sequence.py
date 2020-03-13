def fib_sequence(n): #defines the function

    if n<= 1:
        return n
    else:
        return(fib_sequence(n-1) + fib_sequence(n-2)) # each number is the sum of the two previous ones
nterms = 25 #how many numbers we want to find.


if nterms <= 0:  #if numbers are less than 0
    print("Enter a postive integer.")
else: #else print
    print("Fibonacci Sequence:")
    for i in range(nterms):
        print(fib_sequence(i))
