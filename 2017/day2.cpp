#include <fstream>
#include <iostream>
#include <sstream>  

using namespace std;

int main()
{

    ifstream input("day2.dat"); // Default mode: ios::in
    if (!input) {
        cerr << "Unable to open input file" << endl;
        return 1;
    }

    string line;

    int n;

    int checksum, lineMax, lineMin;

    while( getline(input, line))
    {
        lineMax = numeric_limits<int>::min();
        lineMin = numeric_limits<int>::max();

        stringstream linestream(line);
    

        while(linestream >> n)
        {
            lineMin = min(lineMin,n);
            lineMax = max(lineMax,n);
            
        }

        checksum += lineMax-lineMin;
    }

    cout << "The checksum was " << checksum << "." << endl;      

    input.close();

    return 0;
}

