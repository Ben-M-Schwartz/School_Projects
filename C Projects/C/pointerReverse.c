#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char input_string[100];
    printf("Please enter a string: \n");
    scanf("%s",input_string);
    printf("String is: %s\n",input_string);

    reverse(s);

    printf("The reversed string is: %s\n",input_string)

    return 0;
}
 
void reverse(char *input_string)
{
   int length, c;
   char *begin, *end, temp;
 
   length = strlen(input_string);
   begin  = input_string;
   end    = input_string;
 
   for (c = 0; c < length - 1; c++)
      end++;
 
   for (c = 0; c < length/2; c++)
   {        
      temp   = *end;
      *end   = *begin;
      *begin = temp;
 
      begin++;
      end--;
   }
}