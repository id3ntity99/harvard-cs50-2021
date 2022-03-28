#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Declare variables
    int startSize, endSize, years;

    // Initialize variable: years
    years = 0;

    // TODO: Prompt for start size
    do
    {
        startSize = get_int("Start Size: ");
    }
    while (startSize < 9);

    // TODO: Prompt for end size
    do
    {
        endSize = get_int("End Size: ");
    }
    while (endSize < startSize);

    // Controlling case: when Start size and End size are same
    if (startSize == endSize)
    {
        printf("Years: 0\n");
    }
    else
    {
        // TODO: Calculate number of years until we reach threshold
        do
        {
            startSize = startSize + (startSize / 3) - (startSize / 4);
            years++;
        }
        while (startSize < endSize);


        // TODO: Print number of years
        printf("Years: %i\n", years);
    }
}