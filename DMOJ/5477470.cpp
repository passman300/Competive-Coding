#include <bits/stdc++.h>
using namespace std;
typedef array<int, 3> arr;
typedef long long ll;
const int MX = 202;

int N, a[MX], dp[MX][MX], ans;
int main()
{
   cin >> N;
    for (int i = 1; i<=N; i++)
    {
        cin >> a[i];
        a[i + N] = a[i];
        dp[i][i] = dp[i + N][i + N] = a[i] % 2;
    }

    for (int len = 1; len < N; len++)
    {
        for (int l = 1, r = l + len; r <= 2 * N; l++, r++)
        {
            dp[l][r] = max(a[l] % 2 - dp[l + 1][r], a[r] % 2 - dp[l][r - 1]);
        }
    }

    for (int i = 1; i <= N; i++)
    {
        if (a[i] % 2 - dp[i + 1][i + N - 1] > 0)
        {
            ans++;
        }
    }
    cout << ans << endl;
}