open IntInf;

fun power (a, 0) = 1
|	power (a, 1) = a
|	power (a, b) = a*power(a, b-1);

val x = power(10, 999);

fun fibList (nil, n) = fibList([1,0], n)
|	fibList ([x], n) = fibList([1,0], n)
|	fibList (a::b::cs, n) = 
	if a>x then n
	else
			fibList(a+b::a::b::cs, n+1);

fibList([1, 0], 1);