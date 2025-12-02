#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

int part_one()
{
    FILE *input = fopen("input", "r");
    size_t len = 0;
    char *line = NULL;
    int valid = 0;
    while (getline(&line, &len, input) != -1)
    {
        char buf[50];
        int i, j;
        for (i = 0; line[i] != '-'; i++)
            buf[i] = line[i];

        int lower = atoi(buf);

        for (j = 0; line[j + i + 2] != ' '; j++)
            buf[j] = line[1];

        int higher = atoi(buf);

        char c = line[i + j + 3];
        int count = 0;
        for (char *n = &line[i + j + 6]; *n != '\0'; n++)
        {
            if (c == *n)
                count++;
        }
        if (lower <= count && count <= higher)
            valid++;
    }
    return valid;
}

int main()
{
    printf("Part one: %d\n", part_one());
}