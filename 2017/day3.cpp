#include <iostream>

using namespace std;

int main()
{
    int square = 361527;
    int steps = 0;

    int ringMax = 1;
    int ringMin = 1;
    int n = 1;

    while (ringMax < square)
    {
        ringMin = ringMax;
        n += 2;
        ringMax = n*n;
    }

    int edgeLength = (ringMax - ringMin) / 4;

    // edgeLength += 1; //adjust for the fact corners only belong to one edge

    cout << n << " " << ringMin << " " << ringMax << " " << edgeLength <<  endl;

    while (ringMin + edgeLength < square)
    {
        ringMin += edgeLength;
    }

    cout << "EdgeMin: " << ringMin << "\n";

    steps = abs(square - (ringMin + edgeLength/2)); // the number of orthogonal steps to take to return to an edge middle
    cout << "Lateral steps: " << steps << ".\n";
    steps += (n-1)/2; //the number of inward steps to take (n is an overestimate at this point)

    
   
    cout << "The steps required for " << square << " are " << steps << "." << endl;      

    return 0;
}

