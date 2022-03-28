#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{

    if (argc == 2 && isdigit(*argv[1]))
    {
        // Save user-set key into variable.
        int key = atoi(argv[1]);

        // Ask user plaintext.
        string plain_text = get_string("plaintext: ");

        // print out string "ciphertext".
        printf("ciphertext: ");

        // Iteration for get each characters from user's plaintext.
        for (int i = 0, n = strlen(plain_text); i < n; i++)
        {
            // Check wether plaintext is alphabetical and lowercase.
            if (plain_text[i] >= 97 && plain_text[i] <= 122)
            {
                // Do encryption.
                char cipher_text = ((plain_text[i] - 97 + key) % 26) + 97;
                printf("%c", cipher_text);
            }

            // Check wheter plaintext is alphabetical and uppercase.
            else if (plain_text[i] >= 65 && plain_text[i] <= 90)
            {
                // Do encryption.
                char cipher_text = ((plain_text[i] - 65 + key) % 26) + 65;
                printf("%c", cipher_text);
            }

            // Handle non-alphbet characters.
            else
            {
                printf("%c", plain_text[i]);
            }
        }
        printf("\n");
    }
    // Handle error if user doesn't cooperate.
    else {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}