#include <stdio.h>
#include <stdlib.h>

int* twoSum(int numbers[], int n, int target)
{
    int i = 0;
    int j = 0;

    int *ptr = (int*)malloc(sizeof(int)*2);

    for (i = 0; i < n; i++)
    {
        for(j = i+1; j < n; j++)
        {
            if(numbers[i] + numbers[j] == target)
            {
                ptr[0] = i+1;
                ptr[1] = j+1;
                return ptr;
            }
        }
    }
}

int main()
{

    int array[] = {3,2,4};

    int target = 6;

    int *ptr = NULL;

    ptr = twoSum(array, sizeof(array)/sizeof(array[0]), target);

    printf("index 1:%d index 2:%d\n", ptr[0], ptr[1]);

    free(ptr);

    return 0;
}
