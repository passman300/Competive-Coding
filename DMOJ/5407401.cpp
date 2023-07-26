#include <bits/stdc++.h>
#define ll long long
using namespace std;
typedef array<int, 4> arr;
const int MX = 86400;

int H, S, Q;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);


    cin >> H;
    cin >> S;
    cin >> Q;

    for (int i = 1; i <= Q; i++)
    {
        H -= S;
        cout << H << endl;
    }
}