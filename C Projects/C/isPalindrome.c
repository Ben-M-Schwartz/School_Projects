#include <stdio.h>
#include <string.h>

void isPalindrome(char string[]){
	
	int l = 0;
	int h = strlen(string) -1;

	int isPalindrome = 1;

	while (h>l) {
		if (string[l] != string[h]){
			printf("This string is not a palindrome \n");
			isPalindrome = 0;
			break;
		}
		else {
			l++;
			h--;
		}
	}

	if (isPalindrome == 1){
		printf("This string is a palindrome \n");
	}

}

int main(){
	isPalindrome("abba"); // output should be "This string is a palindrome"
	isPalindrome("dnd"); // output should be "This string is a palindrome"
	isPalindrome("nerd"); // output should be "This string is not a palindrome"
	return 0;
}