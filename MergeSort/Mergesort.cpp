#include <iostream>
#include <fstream>
using namespace std;

void merge(int arr[], int const p, int const q, int const r)
{
    int const subArray_1 = q - p + 1;
    int const subArray_2 = r - q;

    int* left = new int[subArray_1];
    int* right = new int[subArray_2];

    for (int i = 0; i < subArray_1; i++)
        left[i] = arr[p + i];
    for (int j = 0; j < subArray_2; j++)
        right[j] = arr[q + 1 + j];

    int index1 = 0;
    int index2 = 0;
    int index3 = p;

    while (index1 < subArray_1 && index2 < subArray_2) {

        if (left[index1] <= right[index2]) {
            arr[index3] = left[index1];
            index1++;
        }
        else {
            arr[index3] = right[index2];
            index2++;
        }
        index3++;
    }
    
    while (index1 < subArray_1) {
        arr[index3] = left[index1];
        index1++;
        index3++;
    }
    
    while (index2 < subArray_2) {
        arr[index3] = right[index2];
        index2++;
        index3++;
    }
    delete[] left;
    delete[] right;
}

void divide(int arr[], int const first, int const last)
{
    if (first >= last) return; 

    auto mid = first + (last - first) / 2;
    divide(arr, first, mid);
    divide(arr, mid + 1, last);
    merge(arr, first, mid, last);
}

int main() {
	fstream input;
	input.open("input.txt", ios::in);
	if (!input) {
		cout << "File doesn't exist.";
	}
	else {
		int numOfKeys=0;
		int key;
		input >> numOfKeys;
        if (numOfKeys < 1) {
            cout << "The number of keys is less than 1" << endl;
            return 0;
        }
		int *arr=new int[numOfKeys];
		int i = 0;
		while (i<numOfKeys) {
            if (input.eof())
                break;
			input >> key;
            arr[i] = key;
			i++;
		}

        if (numOfKeys > i) {
            cout << "The number of keys is not correct" << endl;
            cout << "The output file will sort the total amount of Keys." << endl << endl;
            numOfKeys = i;
        }
            
        divide(arr, 0, numOfKeys-1);
        fstream output;
        output.open("output.txt", ios::out);
        if (!output) {
            cout << "File not created!";
        }
        else {
            cout << "File created successfully!";
            output << numOfKeys << endl;
            for (i=0;i<numOfKeys;i++)
                output << arr[i] << endl;
            output.close();
        }
        return 0;
	}

	input.close();
	return 0;
}