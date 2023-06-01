fun isPrime (2, _) = true
|	isPrime (a, b) = 
	if b*b > a then true
	else
		if a mod b = 0 then false
		else isPrime(a, b+1);

fun primeCounter (2, 1) = primeCounter(3, 2)
|	primeCounter (x, 10001) = 
		if isPrime(x, 2) then x
		else primeCounter(x+2, 10001)
|	primeCounter (x, y) = 
		if isPrime(x, 2) then primeCounter (x+2, y+1)
		else primeCounter(x+2, y);

primeCounter (2, 1);
