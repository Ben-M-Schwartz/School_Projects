#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//This function answers the question
int rotate(int *var1, int *var2, int *var3){
	int temp = *var1;
	*var1 = *var3;
	*var3 = *var2;
	*var2 = temp;
}

//The main function simply tests the rotate function
int main(){
	int x = 5;
	int y = 6;
	int z = 7;

	rotate(&x, &y, &z);

	printf("%d, %d, %d", x, y, z);
}