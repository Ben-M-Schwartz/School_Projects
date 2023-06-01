#include <stdio.h>

/*This is my first C Program, it's hello world. This is my main method*/

int main (int argc, char *argv[]){ // start main
	 char ch = "A";
	 int integer = 21; // for converting to Hex (base 16) or Octal (base 8) later
	 float flt = 20.4454;
	 double dbl = 20.123343243;
	 char str[20] = "Louis Yu";
	 printf("Character is %c. \n", ch);
	 printf("String is %s. \n", str);
	 printf("Floating point is %f. \n", flt);
	 printf("Double value is %lf. \n", dbl);
	 printf("Integer value is %d. \n", integer);
	 printf("Octal value is %o. \n", integer);
	 printf("Hexadecimal value is %x. \n", integer);
	 printf("Unsigned integer value is %u. \n", (unsigned) integer)

return 0;
} // end main