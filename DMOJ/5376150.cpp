// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
#define ll long long
using namespace std;
typedef array<int, 3> ar3;
typedef array<int, 4> ar4;
const int MX = 1e5 + 2;

int N;
int dp[MX];
int split[3];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;

    cin >> split[0] >> split[1] >> split[2];

    memset(dp, -0x3f, sizeof dp);

    dp[0] = 0;
    for (int i = 0 ; i < 3; i++)
    {
        for (int j = split[i]; j <= N; j++)
        {
            dp[j] = max(dp[j], dp[j - split[i]] + 1);
        }
    }
    cout << dp[N];
}