#include<stdio.h> // include io library
#include<string.h>
/*This is my first C Program, it's hello world. This is my main method*/

int main (int argc, char *argv[]){ // start main
	if (argc ==2){
		if (strcasecmp(argv[1], "Louis")==0){
			printf("Your argument is Louis");
		}
		else{
			printf("Your argument is not Louis");
		}
	}
	else if (argc >2){
	printf ("Too many arguments\n");
	}

	else{
		printf ("You should at least input one argument\n");
	}

return 0;
} // end main