#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* This declares a structure called Person */
struct Person {
    char name[30];
    unsigned salary;
    unsigned age;
};

struct Person makePerson(char *nm, unsigned sal, unsigned a);
void printPerson(struct Person pp);

int main()
{
	
	struct Person p1, p2;

	p1 =makePerson("John Doe", 4321000u, 40u);
	p2 = makePerson("Alice Rose", 1732000u, 20u);

	printPerson(p1);
	printPerson(p2);


	return 0;
}

struct Person makePerson(char *nm, unsigned sal, unsigned a) {
    struct Person p;
    strcpy(p.name, nm);
    p.salary = sal;
    p.age = a;
    return p;
}

void printPerson(struct Person pp) {
    puts("Person");
    printf("\tname: %s\n", pp.name);
    printf("\tsalary: %u\n", pp.salary);
    printf("\tage: %u\n", pp.age);
}