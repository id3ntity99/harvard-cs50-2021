#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Get user's name
   string name = get_string("What is yout name?\n");

   //Say hello to certain user
   printf("hello, %s\n", name);
}