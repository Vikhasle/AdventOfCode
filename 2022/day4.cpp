#include <iostream>
using namespace std;

int part1(int s0, int e0, int s1, int e1)
{
    if ((s0 <= s1 && e0 >= e1) || (s1 <= s0 && e1 >= e0))
        return 1;
    return 0;
}

int part2(int s0, int e0, int s1, int e1)
{
    if ((s0 <= s1 && e0 >= s1) || (s1 <= s0 && e1 >= s0))
        return 1;
    return 0;
}

int main()
{
    int sum = 0;
    for (string line; getline(cin, line);) {
        int split_point = line.find(",");
        string pair1 = line.substr(0, split_point);
        string pair2 = line.substr(split_point, line.length() - split_point);
        split_point = pair1.find("-");
        int s0 = atoi(pair1.substr(0, split_point).c_str());
        int e0 = atoi(pair1.substr(split_point + 1, pair1.length() - split_point - 1).c_str());
        split_point = pair2.find("-");
        int s1 = atoi(pair2.substr(1, split_point).c_str());
        int e1 = atoi(pair2.substr(split_point + 1, pair2.length() - split_point - 1).c_str());
        // sum += part1(s0, e0, s1, e1);
        sum += part2(s0, e0, s1, e1);
    }
    cout << sum << endl;
    return 0;
}
