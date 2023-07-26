#include <bits/stdc++.h>
using namespace std;
typedef array<int, 3> arr;
const int MX = 1e5 + 5;

int n;
vector<int> lis;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n;
    
    for (int i = 1; i <= n; i++) {
        int x;
        cin >> x;

        if (lis.empty() || lis.back() < x) {
            lis.push_back(x);
        }
        else
        {
            *lower_bound(lis.begin(), lis.end(), x) = x;
        }
    }
    cout << lis.size() << '\n';
}