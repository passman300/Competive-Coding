#include <bits/stdc++.h>
using namespace std;
#define endl '\n';
typedef long long ll;
typedef pair<int, int> pii;
const int MX = 32;
const int MOD = 1e6;


int N;
ll dp[MX];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    dp[0] = 1;
    
    for (int i = 2 ; i <= 30 ; i+=2)
    {
        dp[i] = 3 * dp[i - 2];
        for (int j = i - 4; j >= 0 ; j-=2) dp[i] = (dp[i] + 2 * dp[j]) % MOD;
    }
    
    for (int i = 1, x; i <= 5; i++)
    {
        cin >> x;
        cout << dp[x] << endl;
    }

}