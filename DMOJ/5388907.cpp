#include <bits/stdc++.h>
#define ll long long
using namespace std;
typedef array<int, 3> arr;
const int MX = 1e6 + 2;


int maxTime, maxFull, numRest;
vector<arr> restaurants; // value, time, food serve
int dp[301][101];
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> maxTime >> maxFull >> numRest;

    for (int i = 0; i < numRest; i++)
    {
        int v, t, f;
        cin >> v >> t >> f;

        for (int time = maxTime; time >= t; time--)
        {
            for (int food = maxFull; food >= f; food--)
            {
                dp[time][food] = max(dp[time][food], dp[time - t][food - f] + v);
            }
        }
    }
    cout << dp[maxTime][maxFull];
}