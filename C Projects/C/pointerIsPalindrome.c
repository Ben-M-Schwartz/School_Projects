#include <stdio.h>

void isPalindrome (char* string){
	char *ptr, *rev; // declaring two pointers, one beginning, one end

	ptr = string;
	rev = string;

	int isPalindrome = 1;

	while (*ptr != '\0'){ // start while 1
		ptr ++;
	} // end while 1
		ptr--;

	while (ptr > rev) {
		if (*ptr != *rev){
			isPalindrome = 0;
			printf("This string is not a palindrome \n");
			break;
		}
		else {
			rev++;
			ptr--;
		}
	}	

	if (isPalindrome == 1) {
		printf("This string is a palindrome \n");
	}


}

int main (){
	
	isPalindrome("abba"); // output should be "This string is a palindrome"
	isPalindrome("dnd"); // output should be "This string is a palindrome"
	isPalindrome("nerd"); // output should be "This string is not a palindrome"
	return 0;
}