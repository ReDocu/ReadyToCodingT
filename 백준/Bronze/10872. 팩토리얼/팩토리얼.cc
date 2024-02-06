#include <iostream>

using namespace std;


int factorial(int num)
{
	if (num == 1 || num == 0)
		return 1;

	return num * factorial(num -1);
}

int main()
{
	ios_base::sync_with_stdio(false);
	cout.tie(NULL);
	cin.tie(NULL);

	int num;

	cin >> num;

	cout << factorial(num);

	return 0;
}