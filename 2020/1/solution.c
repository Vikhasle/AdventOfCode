#define _GNU_SOURCE
#define MAX 898083
#include <stdio.h>
#include <stdlib.h>

int part_one(long long input[])
{
    int len = MAX;
    for (int i = 0; i < len; i++)
    {
        for (int j = i + 1; j < len; j++)
        {
            if (input[i] + input[j] == 99920044)
                return input[i] * input[j];
        }
    }
}

int part_two(long long input[])
{

    int len = MAX;
    for (int i = 0; i < len; i++)
    {
        long long a = input[i];
        int start = i + 1;
        int end = len;
        while (start < end)
        {
            long long b = input[start];
            long long c = input[end];
            if (a + b + c == 99920044)
                return a * b * c;
            if (a + b + c > 99920044)
                end -= 1;
            else
                start += 1;
        }
    }
}

int main()
{
    FILE *input = fopen("gy8n81", "r");
    size_t len = 0;
    char *line = NULL;
    long long inp_arr[MAX];
    int i = 0;
    while (getline(&line, &len, input) != -1)
    {
        inp_arr[i] = atoll(line);
        i++;
    }

    //printf("%d\n", part_one(inp_arr));
    printf("%d\n", part_two(inp_arr));
    return 0;
}