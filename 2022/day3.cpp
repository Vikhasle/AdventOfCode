#include <iostream>
using namespace std;

int finddups(string sacks[])
{
    for (int i = 0; i < sacks[0].length(); i++)
        for (int j = 0; j < sacks[1].length(); j++)
            for (int k = 0; k < sacks[2].length(); k++)
                if (sacks[0][i] == sacks[1][j] && sacks[1][j] == sacks[2][k]) {
                    return sacks[0][i] >= 'a' ? sacks[0][i] - 'a' + 1 : sacks[0][i] - 'A' + 27;
                }
    cout << "WHAT DA FACK";
    return -1;
}

int main()
{
    string rucksacks[3];
    int i = 0;
    int sum = 0;
    for (string line; getline(cin, line); i++) {
        rucksacks[i] = line;
        if (i == 2) {
            sum += finddups(rucksacks);
            i = -1;
        }
    }
    cout << sum << endl;
    return 0;
}
