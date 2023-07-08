#include <iostream>
using namespace std;

void veTamGiac(int n, string a[][25])
{
    int saoDau = 0, saoCuoi = n*2;
    for(int i=0; i<n*2+1; i++)
    {
        for(int j=0; j<n*2+1; j++)
        {
            if(j != saoDau && j != saoCuoi)
            {
                a[i][j] = '.';
            }
            a[i][saoDau] = '*';
            
            a[i][saoCuoi] = '*';
//            a[i][j+1] = '\0';
        }
        saoDau ++;
        saoCuoi --;
    }
    for(int i=0; i<n*n+1; i++)
    {
        for(int j=0; j<n*n+1; j++)
        {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    int n;
    cin >> n;
    string a[25][25];
    veTamGiac(n, a);
}
