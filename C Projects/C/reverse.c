#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char input_string[100];
    char reverse[100];
    printf("Please enter a string: \n");
    scanf("%s",input_string);
    printf("String is: %s\n",input_string);


    int j = 0;
    int length = strlen(input_string);
    int i;
 
  	for (i = length - 1; i >= 0; i--)
  	{
  		reverse[j++] = input_string[i];
  	}

 
  	printf("The reversed string is: %s\n", reverse);
  	
  	return 0;
}