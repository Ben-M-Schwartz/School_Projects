#include<stdio.h> 
#include<stdlib.h> 
#include<string.h>
#include <time.h>

int currentMonth=0;
int currentYear=0;
int dayList[] = {31,28,31,30,31,30,31,31,30,31,30,31};
char *week[] =  {"Sunday", "Monday", "Tuesday", "Wednesday",\
 "Thursday", "Friday", "Saturday"};
char *Months[] = {"January", "February", "March", "April",\
 "May", "June", "July", "August", "September",\
  "October", "November", "December"};
int monthWordLength[] = {7, 8, 5, 5, 3, 4, 4, 6, 9, 7, 8, 8};

//To print year, modify the month function to print individual lines

int isLeapYear(int year){//start isLeapYear
	if ((year%4==0 && year%100!=0) || year%400==0)
		{return 1;}
	else 
		{return 0;}

}//end isLeapYear

int printMonth(int day, int month, int year){//start printMonth

	if(isLeapYear(year)==1){//start if
		dayList[1] = 29;
	}//end if

	for (int i=0; i<(19-(monthWordLength[month-1]+5)); i+=2){//start for
		printf(" ");
	}//end for

	printf("%s ", Months[month-1]);
	printf("%d \n", year);
	printf("Su Mo Tu We Th Fr Sa");
	printf("\n");

	for (int i=0; i<day; i++){//start for
		printf("   ");
	}//end for

	for (int i=1; i<=dayList[month-1]; i++){//start for
		printf("%2d", i);
		printf(" ");
		if ((i + day) % 7 == 0){//start if
			printf("\n");
		}//end if
	}//end for
	printf("\n");

return 0;
}//end printMonth

int current(){
	time_t timenow; 
	// time_t is a type suitable for storing the calendar time
	
//struct tm current; 
//this is a structure used to hold time and date
	
	struct tm *current;

// check the time function documentation 
	time(&timenow); 
	// that returns current time aand store in timenow
	
	current = localtime(&timenow); 
	// returns address to struct tm, so tm needs to be address
	
// month needs to plus 1
// year needs to plus 1900

	currentMonth = (current->tm_mon+1);
	currentYear = (current->tm_year+1900); 

	return 0;
}

int dates(int month, int day, int year){ // start dates function
//returns day of the week for given date
if (isLeapYear(year) == 1)
	{dayList[1]=29;}

for(int i = 1753 ; i < year ; i++){ /* start for loop 1*/
	if (isLeapYear(i) == 1)
		day+=366;
	else
		day+=365;

} /*end for loop 1*/

for(int i = 0; i < month-1; i++){ // start for
	day+= dayList[i];
}// end for

return day%7;
} // end dates function


int firstDay[12];
int nextDay[12];


int printMonthForYear(int firstMonth, int year){//start function
//prints 3 months side by side

	//prints the first line of each month
	for(int i = firstMonth; i<firstMonth+3; i++){//start loop
		for (int j=0; j<firstDay[i]; j++){//start loop
			printf("   ");
		}//end loop

		for (int k=1; k<=dayList[i]; k++){//start loop
			printf("%2d", k);
			printf(" ");

			if ((k + firstDay[i]) % 7 == 0){//start if
				printf(" ");
				nextDay[i] = k+1;
				break;
			}//end if
		}//end loop
	}//end loop
	
	//prints the remaining lines of each month
	for(int a = 0; a<5; a++){//start loop
		printf("\n");
		for(int i = firstMonth; i<firstMonth+3; i++){//start loop
			for (int k=nextDay[i]; k<=dayList[i]; k++){//start loop

				//takes into account the last lines
				//If the month is finished add adequate white space
				if(a == 4 && k == dayList[i] || (a==3 && i==1 && \
					firstDay[1] == 0)){//start if
					if((k==30 && dates(i+1, dayList[i], year) == 0) \
						|| (k==31 && \
							dates(i+1, dayList[i], year) == 0) \
						|| (k==31 && \
							dates(i+1, dayList[i], year) == 1)){//start if
						printf("%2d", k);
						break;
					}//end if
					printf("                      ");
					break;
				}//end if

				printf("%2d", k);
				printf(" ");

				if(k == dayList[i]){//start if
					for(int l = 6; \
						l>(dates(i+1, dayList[i], year)); l--){//start loop
						printf("   ");
					}//end loop
					printf(" ");
					nextDay[i] = k;
					break;
				}//end if

				if ((k + firstDay[i]) % 7 == 0){//start if
					printf(" ");
					nextDay[i] = k+1;
					break;
				}//end if
			}//end loop
		}//end loop
	}//end loop
return 0;
}//end function

int printYear(int year) {//start printYear

	if(isLeapYear(year)==1){//start if
		dayList[1] = 29;
	}//end if

	for(int i=0; i<12; i++){//start if
		firstDay[i] = dates(i+1, 1, year);
	}//end if

	printf("                            %d \n", year);
	printf("      January               \
February               March \n");
	printf("Su Mo Tu We Th Fr Sa  Su Mo Tu We \
Th Fr Sa  Su Mo Tu We Th Fr Sa \n");

	printMonthForYear(0, year);
	
	printf("\n");
	printf("\n");

	printf("       April                  \
May                   June \n");
	printf("Su Mo Tu We Th Fr Sa  Su Mo Tu We \
Th Fr Sa  Su Mo Tu We Th Fr Sa \n");

	printMonthForYear(3, year);

	printf("\n");
	printf("\n");

	printf("        July                 \
August              September \n");
	printf("Su Mo Tu We Th Fr Sa  Su Mo Tu We \
Th Fr Sa  Su Mo Tu We Th Fr Sa \n");

	printMonthForYear(6, year);

	printf("\n");
	printf("\n");

	printf("      October               \
November              December \n");
	printf("Su Mo Tu We Th Fr Sa  Su Mo Tu We \
Th Fr Sa  Su Mo Tu We Th Fr Sa \n");

	printMonthForYear(9, year);

	printf("\n");

return 0;
}//end printYear

int main (int argc, char *argv[]){//start main
	current();

	if(argc == 1){//beginif
		printMonth(dates(currentMonth, 1, currentYear), \
			currentMonth, currentYear);
	}//end if

	else if (argc ==2){//begin else if
		if (atoi(argv[1])>0){//begin if
			if(atoi(argv[1])<1753) {//beginif
				printf("Please enter a year after 1753\n");
			}//end if
			else{//begin else
			printYear(atoi(argv[1]));
			}//end else
		}//end if
		else{//begin else
			printf("Please enter a valid input \n");
		}//end else
	}//end else if

	else if (argc==3){//begin else if
		int month = 0;

		//checks for reference to month by name
		//e.g March instead of 3
		for (int i=0; i<12; i++){//begin loop
			if(strncasecmp(argv[1], Months[i], 3) == 0 \
				|| strncasecmp(argv[2], Months[i], 3) == 0){//begin if
				month = i+1;
			}//end if
		}//end loop
		if(strcmp((argv[1]), "-m") == 0 && atoi(argv[2]) > 0 \
		&& atoi(argv[2]) <= 12){//begin if
			month = atoi(argv[2]);
			printMonth(dates(month, 1, currentYear),\
			 month, currentYear);
		}//end if
		else if(strcmp((argv[1]), "-m") == 0 && month >0){//begin else if
			printMonth(dates(month, 1, currentYear),\
			 month, currentYear);
		}//end else if
		else if(atoi(argv[1]) >= 1 && atoi(argv[1]) <=12 && \
				atoi(argv[2]) > 0) {//begin else if
			if(atoi(argv[2])<1753) {//begin if
				printf("Please enter a year after 1753\n");
			}//end if
			else{//begin else
				month = atoi(argv[1]);
				int year = atoi(argv[2]);
				printMonth(dates(month, 1, year), month, year);
			}//end else
		}//end else if
		else if(month > 0 && atoi(argv[2]) > 0){//begin else if
			if(atoi(argv[2])<1753) {//begin if
				printf("Please enter a year after 1753\n");
			}//end if
			else{//begin else
				int year = atoi(argv[2]);
				printMonth(dates(month, 1, year), month, year);
		}//end else
		}//end else if
		else{//begin else
			printf("Please enter a valid input \n");
		}//end else
	}//end else if

	else if (argc == 4){//begin else if
		int month = 0;
		for (int i=0; i<12; i++){//begin loop
			if(strncasecmp(argv[1], Months[i], 3) == 0 || \
				strncasecmp(argv[2], Months[i], 3) == 0){//begin if
				month = i+1;
			}//end if
		}//end loop

		if(strcmp((argv[1]), "-m") == 0 && atoi(argv[2]) >= 1 && \
			atoi(argv[2]) <= 12 && atoi(argv[3])>0){//begin if
			if(atoi(argv[3])<1753) {//begin if
				printf("Please enter a year after 1753\n");
			}//end if
			else{//begin else
				int month = atoi(argv[2]);
				int year = atoi(argv[3]);
				printMonth(dates(month, 1, year), month, year);
			}//end else
		}//end if

		else if(strcmp((argv[1]), "-m") == 0 && month > 0 && \
				atoi(argv[3])>0){//begin else if
			if(atoi(argv[3])<1753) {//begin if
				printf("Please enter a year after 1753\n");
			}//end if
			else{//begin else
				int year = atoi(argv[3]);
				printMonth(dates(month, 1, year), month, year);
			}//end else
		}//end else if

		else{//begin else
			printf("Please enter a valid input \n");
		}//end else


	}//end else if
return 0;
}//end main