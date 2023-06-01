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

person_t *makePerson(char *nm, unsigned sal, unsigned a);
void printPerson(person_t *pp);

int main()
{
    person_t *jdoep = makePerson("John Doe", 4321000u, 40u);
    person_t *arosep = makePerson("Alice Rose", 1732000u, 20u);

    puts("Here are our people.");
    printPerson(jdoep);
    printPerson(arosep);
    
    return 0;
}

/*
* Allocates a 'struct Person' on the heap, initializes its fields,
* and returns a pointer to it.
*
* This shows that a function can return a pointer to a structure.
*/
person_t *makePerson(char *nm, unsigned sal, unsigned a) {
    person_t *pp = (person_t *) malloc(sizeof(person_t));
    strcpy(pp->name, nm);
    pp->salary = sal;
    pp->age = a;
    return pp;
}

/*
* Prints the 'struct Person' object pointed by 'pp'.
*
* This shows that a pointer to a structure can be passed as an argument to a function.
*/
void printPerson(person_t *pp) {
    puts("Person");
    printf("\tname: %s\n", pp->name);
    printf("\tsalary: %u\n", pp->salary);
    printf("\tage: %u\n", pp->age);
}