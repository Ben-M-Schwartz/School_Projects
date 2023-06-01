#include <stdio.h>
#include <stdlib.h>

int printMonth(){

	printf("Su Mo Tu We Th Fr Sa");
	printf("\n");
	for (int i=1; i<=31; i++){
		printf("%2d", i);
		printf(" ");
		if (i % 7 == 0){
			printf("\n");
		}
	}
	printf("\n");

return 0;
}

int main (int argc, char*argv[]){

printMonth();

return 0;
}