// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 100000;

// Init size of dictionary to 0.
int dict_size = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // Hash word to obtain hash value
    int hash_value = hash(word);
    // Access linked list at that index in hash table
    node *n = table[hash_value];
    // Traverse linked list, looking for word (strcasecomp)
    while (n != NULL)
    {
        if (strcasecmp(word, n->word) == 0)
        {
            return true;
        }
        n = n->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO
    long sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        sum += tolower(word[i]);
    }
    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *infile = fopen(dictionary, "r");
    if (infile == NULL)
    {
        printf("Cannot load dictionary: The file may not exsist...");
        return false;
    }

    char file_string[LENGTH + 1];

    while (fscanf(infile, "%s", file_string) != EOF)
    {
        // Create new node.
        node *n = malloc(sizeof(node));
        // Check NULL
        if (n == NULL)
        {
            printf("Cannot allocate memory.");
            return false;
        }

        // Copy strings to new node.
        strcpy(n -> word, file_string);

        int hash_code = hash(file_string);

        n -> next = table[hash_code];
        table[hash_code] = n;

        dict_size++;
    }

    fclose(infile);
    // TODO
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return dict_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    // Iterate over hash table and free nodes in each linked list
    for (int i = 0; i < N; i++)
    {
        // Assign cursor
        node *n = table[i];
        // Loop through linked list
        while (n != NULL)
        {
            // Make temp equal cursor;
            node *tmp = n;
            // Point cursor to next element
            n = n->next;
            // free temp
            free(tmp);
        }
        if (n == NULL && i == N - 1)
        {
            return true;
        }
    }
    return false;
}
