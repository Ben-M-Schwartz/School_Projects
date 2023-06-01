open IntInf;

fun isPrime (2, _) = true
|	isPrime (3, _) = true
|	isPrime (a, b) = 
	if b*b > a then true
	else
		if a mod b = 0 then false
		else isPrime(a, b+2);

fun primeCounter (x, y, n) = 
		if y = n then x
		else
			if isPrime(x, 3) then primeCounter (x+2, y+1, n)
			else primeCounter(x+2, y, n);

fun prime 1 = 2
|	prime 2 = 3
|	prime n = primeCounter(3, 2, n);

prime 10001;