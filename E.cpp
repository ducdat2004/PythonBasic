#include <iostream>
#include <cmath>
using namespace std;


int main()
{
    double n;
    cin >> n;
    double x = 1/n;
    double e = 1e-9;
    for(double i = 1; i <= 200; i++)
    {
        for(double j = 1; j <= 200; j++)
        {
            double a = (1/i) + (1/j);

            if (abs(a - x) < e)
                cout << i << " " << j << endl;
        }
    }
}