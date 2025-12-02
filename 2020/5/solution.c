#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define _GNU_SOURCE
#define MAX 259837
#define LINE_LEN 18
int part_one(int *inp)
{
    int m = 0;
    for (int i = 0; i < MAX; i++)
    {
        if (inp[i] > m)
            m = inp[i];
    }
    return m;
}

int part_two(int *inp)
{
    double s, s2;
    int max = 0;
    int min = inp[0];
    for (int i = 0; i < MAX; i++)
    {
        if (inp[i] > max)
            max = inp[i];
        if (inp[i] < min)
            min = inp[i];
        s += inp[i];
    }
    for (int i = min; i <= max; i++)
        s2 += i;
    return s2 - s;
}

int convert(char *n)
{
    unsigned int res = 0;
    unsigned int power = pow(2, LINE_LEN - 1);
    while (*n != '\n')
    {
        if (*n == 'B' || *n == 'R')
            res += (1) * power;
        else if (*n == 'F' || *n == 'L')
            res += (0) * power;
        power /= 2;
        n++;
    }
    return res;
}

int main()
{
    FILE *input = fopen("bigboy", "r");
    size_t len = 0;
    char *line = NULL;
    int inp_arr[MAX];
    int i = 0;
    while (getline(&line, &len, input) != -1)
    {
        inp_arr[i] = convert(line);
        i++;
    }
    printf("Part one: %d\n", part_one(inp_arr));
    printf("Part two: %d\n", part_two(inp_arr));
    return 0;
}