#include <stdio.h>
#include <stdlib.h>


int dayList[] = {31,28,31,30,31,30,31,31,30,31,30,31};
char *week[] =  {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

int isLeapYear(int year){
	if ((year%4==0 && year%100!=0) || year%400==0)
		{return 1;}
	else 
		{return 0;}

}

int dates(int month, int day, int year){ // start dates function
if (isLeapYear(year) == 1)
	{dayList[1]=29;}

if (year<1753 || month<1 || month >12 || day< 1 || day >dayList[month-1]){printf("Not a valid date\n");}

for(int i = 1753 ; i < year ; i++){ /* start for loop 1*/
	if (isLeapYear(i) == 1)
		day+=366;
	else
		day+=365;

} /*end for loop 1*/

for(int i = 0; i < month-1; i++){ // start for
	day+= dayList[i];
}// end for

printf("%s\n", week[day % 7]);
return 0;
} // end dates function


int main (int argc, char* argv[]){ // start main	
int month = atoi(argv[1]);
int day = atoi(argv[2]);
int year = atoi(argv[3]);
dates(month, day, year);

return 0;
} // end main
