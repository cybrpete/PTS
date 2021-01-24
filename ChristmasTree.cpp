#include <iostream>
using namespace std;

int main ()
{
	int iter;
	int orig;

	cout << "How high do you want your tree? ";
	cin >> iter;
	orig = iter;

	while (iter > 0){

		for (int i = iter - 1; i > 0; i--){
			cout << " ";
		}

		for (int i = 0; i < (orig - iter) * 2 + 1; i++){
			cout << "*";
		}

		cout << "\n";
		iter--;
	}

	cin.ignore();
	return 0;
}
