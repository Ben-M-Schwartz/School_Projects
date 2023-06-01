open IntInf;
fun fact1 (0, acc) = acc
|	fact1 (n, acc) = fact1(n-1, acc*n)

fun fact n = fact1(n,1)

fun sum n = 
	if n<10 then n
	else n mod 10 + sum(n div 10);

fun factDigitSum n = sum(fact(n));

factDigitSum 100;