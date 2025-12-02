#include <iostream>
using namespace std;

int point_table[255];

int part1(char O, char P)
{
    int res = point_table[O] - point_table[P];
    if (res < 0)
        res += 3;
    if (res == 1)
        return point_table[P];
    if (res == 2)
        return 6 + point_table[P];
    return 3 + point_table[P];
}

int part2(char O, char P)
{
    switch (P) {
    case 'Y':
        return 3 + point_table[O];
    case 'X':
        return point_table[O] - 1 > 0 ? point_table[O] - 1 : 3;
    case 'Z':
        return 6 + (point_table[O] == 3 ? 1 : point_table[O] + 1);
    }
}

int main()
{
    point_table['A'] = 1;
    point_table['X'] = 1;
    point_table['B'] = 2;
    point_table['Y'] = 2;
    point_table['C'] = 3;
    point_table['Z'] = 3;
    int p1_score = 0;
    int p2_score = 0;
    for (string line; getline(cin, line);) {
        p1_score += part1(line[0], line[2]);
        p2_score += part2(line[0], line[2]);
    }
    cout << p1_score << endl;
    cout << p2_score << endl;
    return 0;
}
