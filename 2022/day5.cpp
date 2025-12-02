#include <cstring>
#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int sum = 0;
    vector<char> crates[9];
    for (string line; getline(cin, line);) {
        if (line == "")
            break;
        strtok(line.c_str(), " ");
    }
    return 0;
}
