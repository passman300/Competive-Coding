#include <bits/stdc++.h>
#define ll long long
using namespace std;
const int MX = 1e6 + 2;

int main()
{

    int N, W;
    cin >> N >> W;
    vector<ll> wt;
    vector<ll> val;
    for (int i = 0; i < N; i++) {
        ll t1, t2;
        cin >> t1 >> t2;
        wt.push_back(t1);
        val.push_back(t2);
    }
    ll i, j;
    int n = N;
    vector<vector<ll>> DP(n + 1, vector<ll>(W + 1, 0));

    // Build table K[][] in bottom up manner
    for (i = 1; i < n+1; i++)
    {
        for (j = 1; j<W +1; j++)
        {
            if (wt[i - 1] <= j)
                DP[i][j] = max(val[i - 1] +
                               DP[i - 1][j - wt[i - 1]],
                               DP[i - 1][j]);
            else
                DP[i][j] = DP[i - 1][j];
        }
    }
    cout << DP[n][W] << endl;
}