#include <bits/stdc++.h>
#define ll long long
using namespace std;
const int MX = 1e6 + 2;

int N;
int prices[MX];
int dp[MX];

void dpChoices(int i)
{
    int a, b, c;
    a = dp[max(0, i - 1)] + prices[i];

    b = dp[max(0, i - 2)] + (prices[i] + prices[i - 1]) - min(prices[i], prices[i - 1]) * 0.25;

    c = dp[max(0, i - 3)] + (prices[i] + prices[i - 1] + prices[i - 2]) - min(prices[i], min(prices[i - 1], prices[i - 2])) * 0.5;


    dp[i] = min(a, min(b, c));
}



int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    for (int i = 1; i <= N; i++)
    {
        cin >> prices[i];
    }

    dp[0] = 0;
    for (int i = 1; i <= N; i++)
    {
        dpChoices(i);
    }

    cout << dp[N];
}