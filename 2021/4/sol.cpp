#include <cstdio>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cstring>
using namespace std;

void split(string str, vector<string>* container, char c)
{
	int j = 0;
	for (int i = 1; i < str.length(); i++) {
		if (str[i] == c) {
			container->push_back(str.substr(j, i - j));
			j = i + 1;
			while (str[j] == c) j++, i++;
		}
	}
	container->push_back(str.substr(j, str.length() - 1));
}

bool contains(int x, vector<int> container)
{
	for (int i = 0; i < container.size(); i++)
		if (container[i] == x)
			return true;
	return false;
}

bool check_win(vector<int> marked)
{
	for (int i = 0; i <= 20; i += 5) {
		bool won = true;
		for (int j = i; j <= i + 4; j++)
			if (!contains(j, marked))
				won = false;
		if (won)
			return true;
	}
	for (int i = 0; i <= 4; i++) {
		bool won = true;
		for (int j = i; j <= i + 20; j += 5)
			if (!contains(j, marked)) {
				won = false;
				break;
			}
		if (won)
			return true;
	}
	bool won = true;
	for (int j = 0; j <= 24; j += 6)
		if (!contains(j, marked)) {
			won = false;
			break;
		}
	if (won)
		return true;
	for (int j = 4; j <= 20; j += 4)
		if (!contains(j, marked)) {
			won = false;
			break;
		}
	return won;
}

int bingo(int board[], vector<string> draws)
{
	vector<int> marked;
	int c = 0;
	for (int i = 0; i < draws.size(); i++, c++) {
		int num = stoi(draws[i]);
		int j;
		for (j = 0; j < 25 && board[j] != num; j++)
			;
		if (j < 25)
			marked.push_back(j);
		if (check_win(marked))
			return c;
	}
	return c;
}

int score(int* board, vector<string> draws, int num_draws)
{
	int sum = 0;
	for (int i = 0; i < 25; i++){
		int j;
		int num = stoi(draws[0]);
		for (j = 0; j <= num_draws && board[i] != num; j++, num = stoi(draws[j]))
			;
		if (j > num_draws){
			sum += board[i];
		}
	}
	return sum * stoi(draws[num_draws]);
}

int main()
{
	fstream file = fstream("input");
	vector<string> draws;
	string line;
	getline(file, line);
	split(line, &draws, ',');
	int least_draws = draws.size();
	int most_draws = 0;
	int best_board[25];
	int worst_board[25];
	int board[25];
	while (file.peek() != EOF) {
		getline(file, line);
		for (int j = 0; j < 5; j++) {
			getline(file, line);
			vector<string> nums;
			split(line, &nums, ' ');
			for (int k = 0; k < nums.size(); k++){
				board[5 * j + k] = stoi(nums[k]);
			}
		}
		int num = bingo(board, draws);
		if (num < least_draws) {
			least_draws = num;
			for (int i = 0; i < 25; i++)
				best_board[i] = board[i];
		}
		if (num > most_draws) {
			most_draws = num;
			for (int i = 0; i < 25; i++)
				worst_board[i] = board[i];
		}
	}
	cout << "Part 1" << endl;
	cout << score(best_board, draws, least_draws) << endl;
	cout << "Part 2" << endl;
	cout << score(worst_board, draws, most_draws) << endl;
	return 0;
}
