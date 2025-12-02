#include <fstream>
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main()
{

    fstream file = fstream("input");
    string line;
    map<pair<int, int>, int> postions;

    while (getline(file, line)) {
        int x1, x2, y1, y2;
        int split_pos = line.find("->");
        string pos1 = line.substr(0, split_pos);
        string pos2 = line.substr(split_pos + 2, line.length());
        split_pos = pos1.find(",");
        x1 = stoi(pos1.substr(0, split_pos));
        y1 = stoi(pos1.substr(split_pos + 1, pos1.length()));
        split_pos = pos2.find(",");
        x2 = stoi(pos2.substr(0, split_pos));
        y2 = stoi(pos2.substr(split_pos + 1, pos2.length()));
        if (x1 == x2) {
            int start = min(y1, y2);
            int end = max(y1, y2);
            for (int i = start; i <= end; i++) {
                pair<int, int> pos(i, x1);
                if (postions.find(pos) != postions.end())
                    postions[pos]++;
                else
                    postions[pos] = 1;
            }
        } else if (y1 == y2) {
            int start = min(x1, x2);
            int end = max(x1, x2);
            for (int i = start; i <= end; i++) {
                pair<int, int> pos(y1, i);
                if (postions.find(pos) != postions.end())
                    postions[pos]++;
                else
                    postions[pos] = 1;
            }
        } else {
            int vel_y = (y2 - y1) / abs(y2 - y1);
            int vel_x = (x2 - x1) / abs(x2 - x1);
            for (int i = x1, j = y1; i != x2 + vel_x; i += vel_x, j += vel_y) {
                pair<int, int> pos(j, i);
                if (postions.find(pos) != postions.end())
                    postions[pos]++;
                else
                    postions[pos] = 1;
            }
        }
    }
    int c = 0;
    for (auto& x : postions)
        if (x.second >= 2)
            c++;
    cout << c << endl;
    return 0;
}
