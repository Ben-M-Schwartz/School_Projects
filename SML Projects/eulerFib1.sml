open IntInf;
fun fib1 (0, acc1, acc2) = 0
|	fib1 (1, acc1, acc2) = acc2
|	fib1 (n, acc1, acc2) = fib1(n-1, acc2, acc1 + acc2);

fun fib n = fib1(n, 0, 1);

fun power (a, 0) = 1
|	power (a, 1) = a
|	power (a, b) = a*power(a, b-1);

val x = power(10, 999)

fun main n = 
	if fib n > x then n
	else main(n+1);

main 1;