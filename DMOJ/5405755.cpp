#include <bits/stdc++.h>
#define ll long long
using namespace std;
typedef array<int, 4> arr;
const int MX = 86400;

int N, M;
int a[MX];
int sum;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);


    cin >> N;
    for (int i = 1; i <= N; i++)
    {
        cin >> a[i];
        sum += a[i];
    }

    int half = sum / 2;
    bool dp[half + 1];
    for (int i = 0 ; i <= half + 1; i++) dp[i] = false;

    dp[0] = true;

    for (int i = 1; i <= N; i++)
    {
        for (int j = half; j >= a[i]; j--)
        {
            if (dp[j - a[i]]) dp[j] = true;
        }
    }


    for (int i = half; i >= 0; i--)
    {
        if (dp[i])
        {
            int t1 = i, t2 = sum - i;
            cout << abs(t1 - t2);
            return 0;
        }
    }

}