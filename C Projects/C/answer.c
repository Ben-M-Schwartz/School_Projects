#include <stdio.h>
#include <string.h>

int main(){
	int x = -2^31;
	int y = -20;
	int z = -1;

	unsigned ux = (unsigned) x;
	unsigned uy = (unsigned) y;
	double dx = (double) x;
	double dy = (double) y;
	double dz = (double) z;

	if((x<y) == (-x>-y)){
		printf("1");
	}
	else{
		printf("0");
	}

	if((~x+~y+1) == (~(x+y))){
		printf("1");
	}
	else{
		printf("0");
	}

	if(ux-uy == -(y-x)){
		printf("1");
	}
	else{
		printf("0");
	}

	if(((x>>1)<<1) <= x){
		printf("1");
	}
	else{
		printf("0");
	}

	if(dx + dy == (double) (y+x)){
		printf("1");
	}
	else{
		printf("0");
	}

	if(dx + dy + dz == dz + dy + dx){
		printf("1");
	}
	else{
		printf("0");
	}

	if((x >= 0) || (x < ux)){
		printf("1");
	}
	else{
		printf("0");
	}
}
