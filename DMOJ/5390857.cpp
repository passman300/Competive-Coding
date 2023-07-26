#include <bits/stdc++.h>
#define ll long long
using namespace std;
typedef array<int, 4> arr;
const int MX = 1002;


int N, M, K;
int s[MX];
ll dp[MX];
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M >> K;

    // use mixed knapsac
    for (int i = 1, w; i <= N; i++)
    {
        cin >> w >> s[i];

        // do limited knapsac
        for (int j = w; j <= K; j++)
        {
            dp[j] = max(dp[j], dp[j - w] + s[i]);
        }

    }


    // use binary packaging for unlimited knapsac
    for (int i = 1, q, t, d, amount; i <= M; i++)
    {
        cin >> q >> t >> d >> amount;
        for (int k = 1; k <= amount; k*=2)
        {
            int w = k * d;
            ll val = (ll) k * q * s[t];
            amount -= k;

            for (int j = K; j >= w; j--)
            {
                dp[j] = max(dp[j], dp[j - w] + val);
            }
        }

        if (amount > 0) // check if there is remainder
        {
            int w = amount * d;
            ll val = (ll)amount * q * s[t];
            for (int j = K; j >= w; j--)
            {
               dp[j] = max(dp[j], dp[j - w] + val);
            }
        }
    }

    cout << dp[K];
}