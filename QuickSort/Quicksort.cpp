#include <iostream>
#include <fstream>
#include <chrono>
using namespace std;


int partition(int arr[], int start, int end)
{
    int pivot = arr[start];
    int count = 0;
    for (int i = start + 1; i <= end; i++) {
        if (arr[i] <= pivot)
            count++;
    }
    int pivotIndex = start + count;
    swap(arr[pivotIndex], arr[start]);
    int i = start, j = end;
    while (i < pivotIndex && j > pivotIndex) {
        while (arr[i] <= pivot) {
            i++;
        }
        while (arr[j] > pivot) {
            j--;
        }
        if (i < pivotIndex && j > pivotIndex) {
            swap(arr[i++], arr[j--]);
        }
    }
    return pivotIndex;
}

void quickSort(int arr[], int start, int end)
{
    if (start >= end)
    {
        return;
    }
    int p = partition(arr, start, end);
    quickSort(arr, start, p - 1);
    quickSort(arr, p + 1, end);
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
        quickSort(arr, 0, numOfKeys - 1);
        auto end = std::chrono::high_resolution_clock::now();

        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - beg);

        // Displaying the elapsed time
        cout << "Elapsed Time: " << duration.count() << endl;

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