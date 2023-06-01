#include <time.h>
#include <stdio.h>

int main(){
	printcurrent();
	return 0;
}

void printcurrent(){
	time_t timenow; // time_t is a type suitable for storing the calendar time
	
//struct tm current; //this is a structure used to hold time and date
	
	struct tm *current;

// check the time function documentation 
	time(&timenow); // that returns current time aand store in timenow
	
	current = localtime(&timenow); // returns address to struct tm, so tm needs to be address
	

// month needs to plus 1
// year needs to plus 1900

	printf("month %d \n",current->tm_mon+1);
	printf("year %d \n",current->tm_year+1900); 

}