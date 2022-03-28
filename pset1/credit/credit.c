#include <stdio.h>
#include <cs50.h>
#include <math.h>


int main(void)
{
    long long bigInt = get_long_long("Number: ");
    int digits = 16;
    int digit, secondToLast, otherDigits;

    otherDigits = 0;
    secondToLast = 0;

    //Get each digits from user's credit card.
    for (int i = 1; i <= digits; i++)
    {
        // Divide credit card number with 10^i and get remainders(digits).
        long long result = powl(10, i);

        digit = (bigInt % result) / pow(10, i - 1);


        // Get second-to-last digits.
        if (i % 2 == 0)
        {
            //Get Products' digits.
            secondToLast += ((digit * 2) / 10) + ((digit * 2) % 10);
        }
        //Get the other digits.
        else
        {
            otherDigits += digit;

        }

    }

    int checkSum = secondToLast + otherDigits;
    int isValid = checkSum % 10;
    int isSixteen = bigInt / powl(10, 14);
    int isFifteen = bigInt / powl(10, 13);
    int isThirteen = bigInt / powl(10, 11);

    //16-digit VISA: first digit is '4' and valid
    if ((isSixteen == 40 || isSixteen == 41 || isSixteen == 42) && isValid == 0)
    {
        printf("VISA\n");
    }

    //13-digit VISA: first digit is '4' and valid
    else if ((isThirteen == 40 || isThirteen == 41 || isThirteen == 42) && isValid == 0)
    {
        printf("VISA\n");
    }


    //15-digit AMEX: first digit is '3' and valid
    else if (isFifteen == 37 && isValid == 0)
    {
        printf("AMEX\n");
    }


    //16-digit MasterCard: first digit is '2' and valid
    else if ((isSixteen == 22 || isSixteen == 51 || isSixteen == 55) && isValid == 0)
    {
        printf("MASTERCARD\n");
    }


    //Unvalid card number.
    else
    {
        printf("INVALID\n");
    }
}

