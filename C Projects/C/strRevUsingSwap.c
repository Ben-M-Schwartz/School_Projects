#include <stdio.h>
#include <string.h>

/*This function takes in two variables as separate 
parameters and rotates the values stored*/
void swap(char *var1, char *var2){
  char temp1 = *var2;
  *var2 = *var1;
  *var1 = temp1;
}


void main(){
	char arrayElement[50];

	/*Request input from the user.
	Takes argument in without spaces*/
	printf("input a string to reverse: ");
	scanf("%s", arrayElement);

	int size =strlen(arrayElement);
	
	for(int i = 0; i < size/2; i++){
		swap(&arrayElement[i],&arrayElement[size-i-1]);
		
	}
	printf("The reversed string is: %s \n",arrayElement);
	
}