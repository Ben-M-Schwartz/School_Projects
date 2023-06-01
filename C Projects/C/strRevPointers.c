#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int reverseString(char* string){
    char *pointer = string;
    char *pointer2 = string;

    while(*pointer2 != '\0'){
        pointer2 ++;
    }
    pointer2 --;

    while(pointer < pointer2){
        char temp = *pointer;
        *pointer = *pointer2;
        *pointer2 = temp;
        pointer ++;
        pointer2 --;
    }

    return 0;
}

int main()
{
    /*int i;
    char string[100],temp;
    printf("Please enter a string: \n");
    scanf("%s",string);
    printf("String is: %s\n",string);
    char *ptr = string;
    while(*ptr != '\0'){
        ptr++;
        i++;
    }
    printf("REVERSE STRING IS: ");
    while(i>=0){
        printf("%c",*ptr);
        i--;
        ptr--;
    }
    printf("%c\n",'\0');
    return 0;*/


    char string[100]  = "Reverse This String";
    printf("%s\n", string);

    reverseString(string);

    printf("%s\n", string);
}