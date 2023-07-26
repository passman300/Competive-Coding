#include <bits/stdc++.h>
using namespace std;
typedef array<int, 3> arr;
const int MX = 1e5 + 5;

string line;


vector<int> A;
vector<int> B;
vector<int> C;

int ans; // max sum

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    for (int lines = 0; lines < 3; lines++)
    {
        int x;
        cin >> x;
        A.push_back(x);
    }
    for (int lines = 0; lines < 3; lines++)
    {
        int x;
        cin >> x;
        B.push_back(x);
    }
    for (int lines = 0; lines < 3; lines++)
    {
        int x;
        cin >> x;
        C.push_back(x);
    }

    for (int i = 0 ; i < 3; i++)
    {
        int j = i - 1;
        if (j == -1)
        {
            j = 2;
        }

        if (B[i] == A[j] && C[i] >= 0)
        {
            ans += C[i];
        }
    }

    cout << ans;

}