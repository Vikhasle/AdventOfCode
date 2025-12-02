#include <fstream>
#include <iostream>
using namespace std;

void part_one()
{
    ifstream file("input");
    string line;
    int count = 0;
    int last = -1;
    getline(file, line);
    while (!line.empty()) {
        int n = stoi(line);
        if (n > last)
            count++;
        last = n;
        getline(file, line);
    }
    cout << count << '\n';
}

void part_two()
{
    ifstream file("input");
    string line;
    int count = 0;
    int last[3] = { -1, -1, -1 };
    for (int i = 0; i < 3; i++) {
        getline(file, line);
        last[i] = stoi(line);
    }
    while (!line.empty()) {
        int n = stoi(line);
        if (n > last[0])
            count++;
        for (int i = 0; i < 2; i++)
            last[i] = last[i + 1];
        last[2] = n;
        getline(file, line);
    }
    cout << count << '\n';
}

int main()
{
    part_one();
    part_two();
    return 0;
}
