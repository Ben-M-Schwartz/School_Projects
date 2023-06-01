fun intsFromTo (a,b) =
		if (a<=b) then a::intsFromTo(a+1, b)
		else nil;

fun take (nil, a) = nil
|	take (x::xs, a) =
		if (a>0) then x::take(xs, a-1)
		else nil;

fun drop (nil, a) = nil
|	drop (x::xs, a) = 
		if (a>1) then drop(xs, a-1)
		else xs;

fun interleave (nil, ys) = ys
|	interleave (xs, nil) = xs
|	interleave (x::xs, y::ys) =
		x::y::interleave(xs,ys);

fun shuffle nil = nil
|	shuffle (x) = 
		let
			val l = length(x)
		in 
			if(l mod 2 = 0) then interleave(take(x, l div 2), drop(x, l div 2))

			else interleave(take(x, (l div 2)+1), drop(x, l div 2 +1))
		end;

fun isInOrder nil = true
|	isInOrder [x] = true
|	isInOrder (x::xs) = 
		if(x < hd(xs)) then isInOrder(xs)
		else false;

fun shuffleNumber a = 
	if (a<2) then 0
	else
	let
	fun check (x, y) = 
		if (isInOrder(shuffle(x))) then y
		else check (shuffle(x), y+1);
	in 
		check(intsFromTo(1, a), 1)
	end;

map shuffleNumber [5, 50, 500, 5000];

(*Here is a list of functions and their inferred types.	
	intsFromTo = fn : int * int -> int list

	take = fn : 'a list * int -> 'a list

	drop = fn : 'a list * int -> 'a 

	interleave = fn : 'a list * 'a list -> 'a list

	shuffle = fn : 'a list -> 'a list

	isInOrder = fn : int list -> bool

	shuffleNumber = fn : int -> int

Output for map shuffleNumber [5, 50, 500, 5000]

val it = [4,21,166,357] : int list*)

	