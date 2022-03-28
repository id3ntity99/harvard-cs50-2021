#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Init variables.
    int jpeg_counter = 0;
    char filename[8];
    FILE *out = NULL;
    BYTE buffer[512];

    // Check Usssage.
    if (argc != 2)
    {
     printf("Wrong Usage: ./recover file\n");
    }

    // open memory card.
    FILE *file = fopen(argv[1], "r");
    if (!file)
    {
        printf("No files detected.\n");
        return 1;
    }

    // Repeat untill end of file.
    while(fread(buffer, sizeof(buffer), 1, file) == 1)
    {

        // If start of new JPEG:
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If first jpeg.
            if (jpeg_counter == 0)
            {
                // Make file name.
                sprintf(filename, "%03d.jpg", jpeg_counter);
                // Open new JPEG.
                out = fopen(filename, "w");
                fwrite(buffer, sizeof(buffer), 1, out);
                jpeg_counter ++;

            }
            else if (jpeg_counter > 0)
            {
                fclose(out);
                sprintf(filename, "%03d.jpg", jpeg_counter);
                out = fopen(filename, "w");
                fwrite(buffer, sizeof(buffer), 1, out);
                jpeg_counter++;
            }
        }

        else
        {
            // If very first blocks of car are not header:
            if (jpeg_counter == 0 )
            {
                continue;
            }

            else
            {
                fwrite(buffer, sizeof(buffer), 1, out);
            }
        }
    }
    // Close every file.
    fclose(out);
    fclose(file);
}

