#include <fstream>
#include <iostream>
#include <math.h>
#include <sstream>
#include <vector>
using namespace std;

double reproduce(int fish, int limit)
{
	if (limit - fish > 0)
		return (limit - fish) + (limit - fish) % 6 * reproduce(8, limit - fish);
	return 0;
}

int main()
{
	fstream file = fstream("input");
	vector<int> lanterfish;
	string line;
	string temp;
	getline(file, line);
	stringstream stream(line);
	while (getline(stream, temp, ','))
		lanterfish.push_back(stoi(temp));

	double c = 0;
	for (int fish : lanterfish)
		c += reproduce(fish, 80);
	cout << c << endl;

	return 0;
}
