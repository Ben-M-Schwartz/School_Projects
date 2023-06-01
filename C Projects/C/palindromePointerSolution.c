#include <stdio.h>

void isPalindrome (char* string){
	char *ptr, *rev;

	ptr = string;

	while (*ptr != '\0'){ // start while 1
	ptr ++;
	} // end while 1
	ptr--;

	rev = string;
	while (ptr >= rev){ // start while 2
	if (*ptr == *rev){
	ptr--;
	rev++;}
	else break;
	
	} // end while 2

	if (rev > ptr)
	puts("String is a palindrone");
	else
	puts("STring is not a palinedrone");

}

int main (){
	
	char str[1000] = "madam";
	isPalindrome(str);

	return 0;
}