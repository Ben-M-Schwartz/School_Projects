#include <stdio.h>
#include <string.h>

void isPalindrome(char str[]){
	
	int l = 0;
	int h = strlen(str) -1;

	while (h > l){ // start while
		if (str[l++] != str[h--]){
		puts ("This string is not a palindrome");
		return;
		}

	} // end while
puts ("This string is a palindrome");

}

int main(){
	isPalindrome("abba");
	isPalindrome("dnd");
	isPalindrome("nerd");
	return 0;
}