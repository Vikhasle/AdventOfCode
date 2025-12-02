#include <fstream>
#include <iostream>
using namespace std;

void part_one()
{
    fstream file = fstream("input");
    string line;
    int pos_x = 0;
    int pos_y = 0;
    while (getline(file, line)) {
        for (int i = 0; i < line.length(); i++)
            if (line[i] == ' ') {
                int x = stoi(line.substr(i + 1, line.length()));
                string op = line.substr(0, i);
                if (op == "forward")
                    pos_x += x;
                else if (op == "down")
                    pos_y += x;
                else if (op == "up")
                    pos_y -= x;
            }
    }
    cout << pos_x * pos_y << '\n';
}

void part_two()
{
    fstream file = fstream("input");
    string line;
    int pos_x = 0;
    int pos_y = 0;
    int aim = 0;
    while (getline(file, line)) {
        for (int i = 0; i < line.length(); i++)
            if (line[i] == ' ') {
                int x = stoi(line.substr(i + 1, line.length()));
                string op = line.substr(0, i);
                if (op == "forward") {
                    pos_x += x;
                    pos_y += aim * x;
                } else if (op == "down")
                    aim += x;
                else if (op == "up")
                    aim -= x;
            }
    }
    cout << pos_x * pos_y << '\n';
}

int main()
{
    part_two();
    return 0;
}
