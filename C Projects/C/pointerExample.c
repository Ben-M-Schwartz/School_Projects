#include <stdio.h>

int main () {
 int x = 2;
 char word[10] = "Hello";

 int *p1;
 p1 = &x;

 printf("%x\n", p1);


 printf("x is %d\n", x);
 printf("Address of x is %x\n", &x);
 printf("Address of Word is %x\n", &word);
 printf("Address of the 3rd element is %x\n", &word[2]);

 *p1 = 10;
 printf("P1 is is now pointed to data %d\n", *p1);
 printf("x is now %d\n", x);


return 0;
}