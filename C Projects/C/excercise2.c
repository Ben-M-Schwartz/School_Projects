#include <stdio.h>

/*
 * isEqual - if x == y  then return 1, else return 0
 *   Example: isEqual(5,5) = 1, isEqual(5,4) = 0
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 5
 */
int isEqual(int x, int y){
	int xor = x ^ y;
	return !xor;
}

int main() {
	int x = isEqual(4, 5);
	int y = isEqual(5, 5);
	int z = isEqual(5, 4);
	printf("%d, %d, %d \n", x, y, z);
return 0;
}