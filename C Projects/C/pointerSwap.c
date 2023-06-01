#include <stdio.h>
#include <stdlib.h>

void swap(int *pointer1,  int *pointer2){
	int temp = *pointer1;
	*pointer1 = *pointer2;
	*pointer2 = temp;

}


int main(int argc, char** argv) {
int x;
int y;
x = 1;
y = 2;

printf ("before: x = %d, y = %d \n", x, y);

swap (&x, &y);

printf ("after: x = %d, y = %d \n", x, y);

return 0;
}