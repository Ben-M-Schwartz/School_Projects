open IntInf;

fun power (a, 0) = 1
|	power (a, 1) = a
|	power (a, b) = a*power(a, b-1);

fun sum n = 
	if n<10 then n
	else n mod 10 + sum(n div 10);

fun powerDigitSum (a, b) = sum(power(a, b));

powerDigitSum(2, 1000);

(*The sum of the digits of 2^1000 is 1366*)