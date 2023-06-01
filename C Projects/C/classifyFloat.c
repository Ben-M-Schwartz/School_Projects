#include <stdio.h>
#include <string.h>

void classify_float(float f){
	unsigned u = *(unsigned*) &f;

	int sign = (u >> 31) & 0x1;

	int exp = (u >> 23) & 0xFF;

	int frac = u & 0x7FFFFF;


	if (exp == 0 && frac == 0)
		printf("Plus or minus zero");
	else if (exp == 0)
		printf("Nonzero, denormalized");
	else if(exp == 0xFF && frac == 0)
		printf("Plus or minus infinity");
	else if(exp == 0xFF)
		printf("NaN");
	else if(exp <= (2^(8-1)-1))
		printf("Greater than -1.0 and less than 1.0");
	else if(sign == 1)
		printf("Less than or equal to -1.0");
	else
		printf("Greater than or equal to 1.0");
}

void main(){
	classify_float(-.5);
}