open IntInf;

fun isMultiple (x, 21) = true
|	isMultiple (x, y) =
		if x mod y = 0 then isMultiple(x, y+1)
		else false;

fun smallestMultiple (x) = 
	if isMultiple (x, 12) then x
	else smallestMultiple(x+(11*13*17*19));

smallestMultiple (11*13*17*19);

(*The smalles number that is a multiple of all the numbers from 1 to 20 is 232792560*)