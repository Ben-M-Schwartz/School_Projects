fun fib1 (0, acc1, acc2) = 0
|	fib1 (1, acc1, acc2) = acc2
|	fib1 (n, acc1, acc2) = fib1(n-1, acc2, acc1 + acc2);

fun fib n = fib1(n, 0, 1);

fib 5;