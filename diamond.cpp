#include <iostream>
using namespace std;
void drawDiamond(int size) {
    // Upper half (including middle row)
    for (int i = 1; i <= size; i++) {
        // Print leading spaces
        for (int s = 0; s < size - i; s++) {
            cout << " ";
        }
        // Print stars
        for (int j = 0; j < 2 * i - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }
    // Lower half
    for (int i = size - 1; i >= 1; i--) {
        // Print leading spaces
        for (int s = 0; s < size - i; s++) {
            cout << " ";
        }
        // Print stars
        for (int j = 0; j < 2 * i - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }
}
int main() {
    int size;
    cout << "Enter the size (number of rows for the upper half): ";
    cin >> size;
    if (size <= 0) {
        cout << "Please enter a positive number." << endl;
        return 1;
    }
    cout << endl;
    drawDiamond(size);
    return 0;
}