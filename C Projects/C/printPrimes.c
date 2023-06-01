#include <stdio.h>
#include <stdlib.h>
#define NUM_PER_LINE 10

int main(int argc, char **argv) { // start main method
int limit = atoi(argv[1]); // take limit from user
int printCount =0;

	for (int i=2; i<= limit; i++){ // start big for
		int isPrime = 1;
		for (int j=2; j< i; j++){ // start small for
			if (i%j == 0){ // start if
				isPrime = 0;
			} // end if
		} // end small for

		if (isPrime == 1){ // start big if 2
			printf("%8d", i);
			printCount++;
			if (printCount == NUM_PER_LINE){ // start small if
				putchar('\n'); // has to use single quote
				printCount = 0;
			} // end small if
		} // end big if 2
	} // end big for

	if (printCount >0){
		putchar ('\n'); // has to use single quote
	}
	return 0;
} // end main method