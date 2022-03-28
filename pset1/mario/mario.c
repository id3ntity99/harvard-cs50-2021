#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Declare variables
    int i, j, bricks;

    do
    {
        //Get user's input for pyramid height
        bricks = get_int("Height: ");
    }
    while (bricks <= 0 || bricks >= 9);

    //Right-aligned pyramid
    for (i = 0; i < bricks; i++)
    {
        for (j = 0; j < bricks; j++)
        {
            //Make if statement:
            if (bricks - 1 <= i + j) {
                printf("#");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
    }

/*
    //Left-aligned pyramid
    for (i = 0; i < bricks; i++)
    {
        for (j = 0; j < bricks; j++)
        {
            //Make if statement: var i is always lareger than or equals to var j when we need to print hashes on screen.
            if (j <= i)
            {
                printf("#");
            }
        }
        printf("\n");
    }
*/
}

