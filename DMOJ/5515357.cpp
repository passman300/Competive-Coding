#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int MM = 1e6 + 3;
const int MOD = 1e9 + 7;


int N;
ll dp[MM];

int main() {
    cin >> N;
    dp[1] = 1;
    dp[2] = 2;
    
    for (int i = 3; i <= N ;i++)
    {
        dp[i] = (dp[i - 1] + 1 + dp[i - 3]) % MOD;
    }
    cout << dp[N];
}