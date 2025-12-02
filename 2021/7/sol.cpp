#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

// sum of 1 to n
int sum(int n)
{
    return n * (n + 1) / 2;
}

long dist(int i, vector<int> lst)
{
    int res = 0;
    for (int crab : lst)
        res += sum(abs(i - crab));
    return res;
}

int main()
{
    fstream file = fstream("input");
    string line;
    string temp;
    vector<int> crabs;
    getline(file, line);
    stringstream stream(line);
    while (getline(stream, temp, ','))
        crabs.push_back(stoi(temp));
    long min = dist(0, crabs);
    for (int i = 1; i < crabs.size(); i++)
        if (dist(i, crabs) < min)
            min = dist(i, crabs);
    cout << min << endl;
    return 0;
}
