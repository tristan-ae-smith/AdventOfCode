#include <fstream>
#include <iostream>

using namespace std;

int main()
{

    ifstream input("day1.dat"); // Default mode: ios::in
    if (!input) {
        cerr << "Unable to open input file" << endl;
        return 1;
    }

    string code;// = "91212129";
    getline(input, code);

    cout << code << endl;

    int total = 0;
    char prev = '\0';

    for (char& c : code)
    {
        // cout << total << endl;
        // cout << c << " " << c - '0' << endl;
        total += (c == prev)? c - '0' : 0;
        prev = c;
    }

    total += (code[0] == prev)? code[0]- '0' : 0;

    cout << "The total was " << total << "." << endl;

    input.close();

    return 0;
}

