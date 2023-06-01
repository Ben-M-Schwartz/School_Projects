#include <stdio.h>
#include <stdlib.h>
#define NUM_PER_LINE 5

int main(int argc, char **argv) { // start main method
int limit = atoi(argv[1]); // take limit from user
int counter = 0;

	for (int i=2; i<= limit; i++){ // start big for
		int isPrime = 1;

		for (int j=2; j< i; j++){ // start small for
			if (i%j == 0){ // start if
				isPrime = 0;
			} // end if
		} // end small for
		if (isPrime == 1){
			counter ++;
			printf("%8d", i);
			if (counter == NUM_PER_LINE){
				printf("\n");
				counter = 0;
			}

		}


	} // end big for



 if (counter >0){
 	putchar ('\n');
 }

	return 0;
} // end main method