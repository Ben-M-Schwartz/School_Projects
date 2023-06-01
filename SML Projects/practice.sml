open Int;

datatype bintree = Empty | Node of int * bintree * bintree;

val t0 = Node (
			4, 
			Node(
						2,
						Node (1, Empty, Empty),
						Node (3, Empty, Empty)
					),
					Node (5, Empty, Empty)
				);

fun contains (Empty, _) = false
|	contains (Node (r, left, right), x) = 
		if (r = x) then true
		else contains(left, x)
		orelse contains(right, x);

fun height(Empty) = ~1
|	height(Node(_, left, right)) = 1 + max(height(left), height(right));

fun mirror (Empty) = Empty
|	mirror (Node(r, left, right)) = Node(r, mirror(right), mirror(left));

fun count (Empty) = 0
|	count (Node(r, left, right)) = 1+count(left)+count(right);

fun countLeaf (Empty) = 0
|	countLeaf (Node(_, left, right)) = 
		if left = Empty andalso right = Empty then 1
		else countLeaf(left) + countLeaf(right);

fun countLeaf2 (Empty) = 0
|	countLeaf2(Node(_, Empty, Empty)) = 1
|	countLeaf2(Node(_, left, right)) = countLeaf2(left) + countLeaf2(right);

fun preorder (Empty) = nil
|	preorder (Node(r, left, right)) = r::preorder(left) @ preorder(right);

fun inorder (Empty) = nil
|	inorder (Node(r, left, right)) = inorder(left) @ r::inorder(right);

fun postorder (Empty) = nil
|	postorder (Node(r, left, right)) = 
		postorder(left) @ postorder(right) @ [r];