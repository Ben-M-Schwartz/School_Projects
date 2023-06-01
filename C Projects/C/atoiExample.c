#include<stdio.h> // include io library
#include<stdlib.h>
#include<string.h>
/*This is my first C Program, it's hello world. This is my main method*/

int main (int argc, char *argv[]){ // start main
	int val;
	char str[20] = "123456";
	
	val = atoi(str);
	printf("Value is %d \n", val);
	strcpy (str, "Louis Yu");
	printf("Value is %d \n", atoi(str));
	printf("Input number plus 10 is %d \n", val+10);
return 0;
} // end main