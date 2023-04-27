#include <iostream>
#include <fstream>
#include <chrono>
using namespace std;


void InsertionSort(int* arr, int size) {

    for (int i = 1; i < size; i++) {
        int key = arr[i];
        int j = i - 1;
        while (key < arr[j] && j >= 0) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
    fstream input;
    input.open("input.txt", ios::in);
    if (!input) {
        cout << "File doesn't exist.";
    }
    else {
        int numOfKeys = 0;
        int key;
        input >> numOfKeys;
        if (numOfKeys < 1) {
            cout << "The number of keys is less than 1" << endl;
            return 0;
        }
        int* arr = new int[numOfKeys];
        int i = 0;
        while (i < numOfKeys) {
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
        auto beg = std::chrono::high_resolution_clock::now();
        InsertionSort(arr, numOfKeys);
        auto end = std::chrono::high_resolution_clock::now();

        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - beg);

        // Displaying the elapsed time
        cout << "Elapsed Time: " << duration.count();
        fstream output;
        output.open("output.txt", ios::out);
        if (!output) {
            cout << "File not created!";
        }
        else {
            cout << "File created successfully!";
            output << numOfKeys << endl;
            for (i = 0; i < numOfKeys; i++)
                output << arr[i] << endl;
            output.close();
        }
        return 0;
    }

    input.close();
    return 0;
}