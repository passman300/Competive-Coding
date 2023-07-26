#include<bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
const int MX = 3001;

int dp[MX][MX];


int N, K;
int main() {
    iostream::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    cin >> K;

    dp[0][1] = 1;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= min(K, i); j++)
        {
            dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j];
        }
    }
    cout << dp[N][K];
}