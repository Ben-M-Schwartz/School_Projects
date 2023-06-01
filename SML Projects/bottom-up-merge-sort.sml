fun makeLists nil = nil
|	makeLists [1] = [[1]]
|	makeLists [x] = [[x]]
|	makeLists (x::xs) = 
		[x] :: makeLists xs;

fun merge (nil, ys) = ys
|	merge (xs, nil) = xs
|	merge (x::xs, y::ys) =
		if(x < y) then x :: merge(xs, y::ys)
		else y :: merge(x::xs, ys);

fun mergeOneRound nil = nil
|	mergeOneRound [cs] = [cs]
|	mergeOneRound (a::b::cs) =
		merge(a, b) :: mergeOneRound(cs);

fun repeatedlyMerge nil = nil
|	repeatedlyMerge [x] = x
|	repeatedlyMerge (a::b) =
		 repeatedlyMerge(mergeOneRound(a::b));

fun mergeSort nil = nil
|	mergeSort x =
		repeatedlyMerge(makeLists(x));

 mergeSort [7, 1, 4, 2, 3];
