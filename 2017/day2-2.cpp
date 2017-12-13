#include <fstream>
#include <iostream>
#include <sstream>  
#include <vector>

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

    int checksum;

    while( getline(input, line))
    {
        stringstream linestream(line);
        vector<int> nums;

        while(linestream >> n)
        {
            nums.push_back(n);            
        }

        for (int a : nums)
        {
            for (int b : nums)
            {
                checksum += (a != b && a % b == 0)? a / b : 0;
            }
        }

    }

    cout << "The checksum was " << checksum << "." << endl;      

    input.close();

    return 0;
}