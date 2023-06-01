#include <stdio.h>
#include <string.h>

int main(){
	int x = 0x8<<28;
	int y = ~x;

	printf("%d, %d", x, y);
}