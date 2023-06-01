def recursiveFib(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return recursiveFib(n-1) + recursiveFib(n-2)



def dpFib(n):
    fibonacci = [0, 1]
    for i in range(2, n+1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    return fibonacci[n]

def main():
    print(recursiveFib(10))
    print(dpFib(10))


main()
