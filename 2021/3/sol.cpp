#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int btoi(string b_str)
{
    int res = 0;
    for (int i = 0; i < b_str.length(); i++) {
        if (b_str[i] == '1')
            res += 1;
        res <<= 1;
    }
    return res;
}

void insert(string b_str, int counter[])
{
    for (int i = 0; i < b_str.length(); i++)
        counter[i] += b_str[i] == '1';
}

void part_one()
{
    fstream file = fstream("input");
    string line;
    getline(file, line);
    int len = line.length();
    int counter[len];
    for (int i = 0; i < len; i++)
        counter[i] = 0;
    int num = 1;
    insert(line, counter);
    while (getline(file, line)) {
        insert(line, counter);
        num++;
    }
    int gamma = 0;
    int eps = 0;
    for (int i = 0; i < len; i++) {
        gamma <<= 1;
        eps <<= 1;
        if (counter[i] > num / 2)
            gamma += 1;
        else
            eps += 1;
    }
    cout << gamma * eps << '\n';
}

void part_two()
{
    fstream file = fstream("test");
    string lines[1000];
    int i = 0;
    while (getline(file, lines[i++]))
        ;
    int counter[lines[0].length()];
    for (int j = 0; j < lines[0].length(); j++)
        counter[j] = 0;
    for (int j = 0; j < i - 1; j++)
        for (int k = 0; k < lines[0].length(); k++)
            counter[k] += (lines[j][k] == '1') ? 1 : -1;
    int ox[lines[0].length()];
    int c2[lines[0].length()];
    for (int j = 0; j < lines[0].length(); j++) {
        ox[j] = counter[j] >= 0;
        c2[j] = !ox[j];
        cout << ox[j];
    }
    cout << endl;
    int c = 1;
    int ox_rat;
    int c2_rat;
    while (c < lines[0].length()) {
        int num_ox = 0;
        int last;
        for (int j = 0; j < i - 1; j++) {
            bool fits = true;
            for (int k = 0; k < c; k++)
                if (ox[k] != (lines[j][k] - '0')) {
                    fits = false;
                    break;
                }
            if (fits)
                num_ox++, last = j;
        }
        if (num_ox == 1) {
            ox_rat = btoi(lines[last]);
            break;
        }
        c++;
    }
    c = 1;
    while (c <= lines[0].length()) {
        int num_c2 = 0;
        int last;
        for (int j = 0; j < i - 1; j++) {
            bool fits = true;
            for (int k = 0; k < c; k++)
                if (c2[k] != (lines[j][k] - '0'))
                    fits = false;
            if (fits)
                num_c2++, last = j;
        }
        if (num_c2 == 1) {
            c2_rat = btoi(lines[last]);
            break;
        }
        c++;
    }
    cout << c2_rat << endl;
    cout << ox_rat << endl;
    cout << c2_rat * ox_rat << endl;
}
int main()
{
    part_two();
    return 0;
}
