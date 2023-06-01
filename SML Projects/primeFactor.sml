open IntInf;

fun isPrime (2, _) = true
|	isPrime (a, b) = 
	if b*b > a then true
	else
		if a mod b = 0 then false
		else isPrime(a, b+1);


fun primeFactors (x, y, a) =
		if x=y then hd a
		else
			if isPrime(x, 2) then
				if x mod y = 0 then primeFactors(x+2, y, x::a)
				else primeFactors(x+2, y, a)
			else primeFactors(x+2, y, a);

primeFactors (3, 13195, []);