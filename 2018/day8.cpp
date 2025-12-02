#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int sum_tree(vector<int> tree, int i, int* sum){
	int j = i + 2;	
	int num_child = tree[i];
	int num_val = tree[i+1];
	for (int k = 0; k < num_child; k++) 
		j = sum_tree(tree, j, sum);
	for (int k = 0; k < num_val; k++){
		*sum += tree[j + k];
	}
	return j + num_val;
}

int sum_tree2(vector<int> tree, int i, int* sum){
	int j = i + 2;	
	int num_child = tree[i];
	int num_val = tree[i+1];
	int sub_sums[num_child];
	if (num_child){
		for (int k = 0; k < num_child; k++){ 
			sub_sums[k] = 0;
			j = sum_tree2(tree, j, &sub_sums[k]);
		}
		for (int k = 0; k < num_val; k++)
			if (tree[j + k]  - 1 < num_child)
				*sum += sub_sums[tree[j + k] - 1];
	}else{
		for (int k = 0; k < num_val; k++)
			*sum += tree[j + k];
	}
	return j + num_val;
}



void part_one()
{
    ifstream file("input8.txt");
    string line;
    getline(file, line);
	vector<int> tree;
	int i = 0;
	while (i < line.length()){
		int split_pos = line.find(" ");
		tree.push_back(stoi(line.substr(0, split_pos)));
		line = line.substr(split_pos + 1, line.length());
		i = split_pos + 1;
	}
	tree.push_back(stoi(line));
	int sum = 0;
	sum_tree(tree, 0, &sum);
	
    cout << sum << endl;
}

void part_two()
{
	ifstream file("input8.txt");
    string line;
    getline(file, line);
	vector<int> tree;
	int i = 0;
	while (i < line.length()){
		int split_pos = line.find(" ");
		tree.push_back(stoi(line.substr(0, split_pos)));
		line = line.substr(split_pos + 1, line.length());
		i = split_pos + 1;
	}
	tree.push_back(stoi(line));
	int sum = 0;
	sum_tree2(tree, 0, &sum);
	
    cout << sum << endl;
}

int main()
{
    part_one();
    part_two();
    return 0;
}
