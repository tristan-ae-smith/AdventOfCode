#include <iostream>
#include <cmath>

using namespace std;

constexpr int limit = 70;
int input = 361527;

int cache[limit]; //the test value of each memory block
int incache[limit]; //the address of the result of stepping inward. Negative if the source is a corner

int get(int n) {return cache[n];}

int pre(int n) {return n-1;}
int post(int n) {return n+1;}
int instep(int n) {return abs(incache[n]);}

bool iscorner(int n) {return incache[n] < 0;}



int main()
{

    //setup the relative inward steps; flag negative if this is a corner

    int relstep = 1;
    int ring = 1;

    cache[1] = 1;
    cache[2] = 1;
    cache[3] = 2;
    cache[4] = 4;
    cache[5] = 5;
    cache[6] = 10;
    cache[7] = 11;
    cache[8] = 23;
    cache[9] = 25;
    cache[10] = 26;
    cache[11] = 54;
    incache[1] = -1; 


    for (int i = 2; i < limit; i++)
    {
        incache[i] = i - relstep;
        //if we're at a precorner
        if ( iscorner(instep(i)) )
        {
            i++;
            incache[i] = -incache[i-1]; //mark post as corner

            relstep+=2;

            //if we're at the end of a ring
            if ( int(sqrt(i)) * int(sqrt(i)) == i)
            {
                i++;
                incache[i] = i-1;
            }
            else if ( i > 10 ) // analytically bypass compactness in inner ring
            {
                i++;   

                incache[i] = i - relstep; //mark postpost as same instep
                
            }
            
 
        }

    }
    for (int i = 12; i < limit; i++)
    {
        // cout << i << ": " << incache[i] << endl;
      
        //analytically:
        // - if it's a new ring, then special cases for transition
        // - if it's a post-corner, then two predecessors and instep corner and post (18)
        // - if it's a pre-corner, then predecessor, instep corner and pre (16)
        // - if it's a corner, then predecessor and instep corner (17)
        // - else:  pre, instep, post, pre
        if (iscorner(post(i)) && int(sqrt(post(i))) * int(sqrt(post(i))) == post(i))
        {
            cache[i] = get(pre(i)) + get(instep(i)) + get(post(instep(i))) + get(pre(instep(i)));
            i++;
            cache[i] = get(pre(i)) + get(instep(i)) + get(post(instep(i)));
            i++;
            cache[i] = get(pre(i)) + get(post(instep(pre(i)))); 
            i++;
            cache[i] = get(pre(i)) + get(pre(pre(i))) + get(instep(i)) + get(post(instep(i)));  
        }
        else if (iscorner(pre(i)))
        {
            cache[i] = get(pre(i)) + get(pre(pre(i))) + get(instep(i)) + get(post(instep(i)));
        }
        else if (iscorner(post(i)))
        {
            cache[i] = get(pre(i)) + get(instep(i)) + get(pre(instep(i)));
        }
        else if (iscorner(i))
        {
            cache[i] = get(pre(i)) + get(instep(i));
        }
        else
        {
            cache[i] = get(pre(i)) + get(instep(i)) + get(post(instep(i))) + get(pre(instep(i)));   
        }

    } 

    for (int i = 1; i < limit; i++)
    {
        cout << i << ": " << get(i) << endl;
    }
    return 0;
}

//IDs
// 17  16  15  14  13
// 18   5   4   3  12
// 19   6   1   2  11
// 20   7   8   9  10  27
// 21  22  23  24  25  26

//relstep
// -5   5   4   3  -3
//  5  -1   1  -1   3
//  6   1   0   1   2
//  7  -1   1  -1   9  10
// -7   7   8   9  -9  25

// stored
// 147  142  133  122   59
// 304    5    4    2   57
// 330   10    1    1   54
// 351   11   23   25   26 1968
// 362  747  806  880  931  957