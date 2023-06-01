#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* This declares a structure called Person */
struct Person {
    char name[30];
    unsigned salary;
    unsigned age;
};

/* This makes 'person_t'  an alias for 'struct Person' */
typedef struct Person person_t;

person_t makePerson(char *nm, unsigned sal, unsigned a);
void printPerson(struct Person pp);

int main()
{
    person_t p1 = makePerson("John Doe", 4321000u, 40u);
    person_t p2 = makePerson("Alice Rose", 1732000u, 20u);

    printPerson(p1);
    printPerson(p2);

    return 0;
}

/*
* Allocates a 'struct Person' on the heap, initializes its fields,
* and returns a pointer to it.
*
* This shows that a function can return a pointer to a structure.
*/
person_t makePerson(char *nm, unsigned sal, unsigned a) {
    person_t p;
    strcpy(p.name, nm);
    p.salary = sal;
    p.age = a;
    return p;
}

void printPerson(person_t pp) {
    puts("Person");
    printf("\tname: %s\n", pp.name);
    printf("\tsalary: %u\n", pp.salary);
    printf("\tage: %u\n", pp.age);
}