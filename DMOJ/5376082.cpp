// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
#define ll long long
using namespace std;
typedef array<int, 3> ar3;
typedef array<int, 4> ar4;
const int MX = 1e4 + 2;

int N;
double dp[MX];


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    double price[1 + N];

    price[0] = 0;
    for (int i = 1; i <= N; i++)
    {
        cin >> price[i];
    }

    dp[0] = 0;
    for (int i = 1; i <= N; i++)
    {
        double a, b, c;

        // choice 1, take full price of new item
        a = dp[i - 1] + price[i];

        // choice 2, group 2, and 50% cheaper
        b = min(price[i - 1], price[i]) * 0.5 + max(price[i - 1], price[i]) + dp[i - 2];

        // choice 3, group 4, and cheapest free
        c = (price[i - 2] + price[i - 1] + price[i]) - min(price[i - 2], min(price[i - 1], price[i])) + dp[i - 3];

        dp[i] = min(a, min(b, c));
    }

    cout << fixed << setprecision(1) << dp[N];
}