#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(void)
{
    node *list = NULL;
    node *n = malloc(sizeof(node));

    if (n != NULL)
    {
        n -> number = 1;
        n -> next = NULL;
    }

    list = n;

    n = malloc(sizeof(node));

    if (n != NULL)
    {
        n -> number = 2;
        n -> next = NULL;
    }

    list -> next = n;

    // Insertion
    n = malloc(sizeof(node));
    if (n != NULL)
    {
        n -> number = 0;
        n -> next = list -> next;
    }


    list -> next = n;

    printf("%i\n", list -> number);
    printf("%i\n", list[0].next->number);


    free(n);
    free(list);
}