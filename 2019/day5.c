#include <stdio.h>

int partOne()
{
}

/*
Re write into c:
function computer(memory) {
        var len = memory.length;
        for (var i = 0; i < len; i += 4) {
            if (memory[i] == 1) {
                memory[memory[i + 3]] = memory[memory[i + 1]] + memory[memory[i + 2]];
            } else if (memory[i] == 2) {
                memory[memory[i + 3]] = memory[memory[i + 1]] * memory[memory[i + 2]];
            } else if (memory[i] == 99) {
                return memory
            }
        }
    }

*/
int computer(int memory[])
{
    int len = sizeof(memory) / sizeof(int);
    for (int i = 0; i < len; i += 4)
    {
        if (memory[i] == 1)
        {
            memory[memory[i + 3]] = memory[memory[i + 1]] + memory[memory[i + 2]];
        }
        else if (memory[i] == 2)
        {
            memory[memory[i + 3]] = memory[memory[i + 1]] * memory[memory[i + 2]];
        }
        else if (memory[i] == 3)
        {
            memory[memory[i + 1]] = getc("Test");
        }
        else if (memory[i] == 4)
        {
            puts(memory[memory[i + 1]]);
        }

        else if (memory[i] == 99)
        {
            return memory;
        }
    }
}

int main()
{
    puts("hei");
    return 0;
}