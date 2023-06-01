#include <stdio.h>
#include <string.h>

void reverse(char *s){
  int len = strlen(s);
  for(len;len>=0;len--){
    printf("%c",s[len]);
  }
}

int main(){
  char word[256];
  printf("Input a string: ");
  scanf("%s",word);
  printf("Reverse of the string is: ");
  reverse(word);
  printf("\n");
  return 0;
}