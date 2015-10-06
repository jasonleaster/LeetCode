#include <stdio.h>
#include <math.h>

int countPrimes(int n)
{
    if (n > 2)
    {
        int table[n];
        table[0] = 2; // counter for primes number we find out
        table[1] = 2;
        table[2] = 3;

        int i = 0;
        int j = 0;
        for(i = 4; i < (int)sqrt(n); i++)
        {
            for(j = 1; j <= table[0]; j++)
            {
                if( i % table[j] == 0)
                {
                    break;
                }
            }

            if(j == table[0] + 1)
            {
                table[j] = i;
                table[0] += 1;
            }
        }

        return table[0];
    }
    else
    {
        return 1;
    }
}

int main()
{
    printf("%d\n", countPrimes(100));
}
