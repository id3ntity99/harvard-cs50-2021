#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int calculate_idx(int letters, int words, int sentences);

int main(void)
{
    // Declare and(or) initialize variables.
    string user_input = get_string("Text: ");
    int i;
    int n = strlen(user_input);
    int letters = 0;
    int words = 1;
    int sentences = 0;

    // Get the number of letters, words, sentences.
    for (i = 0; i < n; i++)
    {
        char letter = tolower(user_input[i]);
        //Check whether letters are alphabets or not.
        if (letter >= 97 && letter <= 122)
        {
            letters++;
        }
        // Detect blank(spacebar) and increments words counts.
        else if (letter == ' ')
        {
            words++;
        }
        // Detect end of the sentence.
        else if (letter == '!' || letter == '?' || letter == '.')
        {
            sentences++;
        }
    }


    // Print out final grade of readability.
    int grade = calculate_idx(letters, words, sentences);

    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

// Function: returns final result(grade) of readability.
int calculate_idx(int letters, int words, int sentences)
{
    float L = ((float) letters / (float) words) * 100;
    float S = ((float) sentences / (float) words) * 100;
    float result = (0.0588 * L) - (0.296 * S) - 15.8;
    return round(result);

}

