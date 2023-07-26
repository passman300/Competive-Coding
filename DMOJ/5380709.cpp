#include <bits/stdc++.h>
#define ll long long
using namespace std;
typedef array<int, 3> ar3;
typedef array<int, 4> ar4;
const int MX = 1e4 + 2;

string line;
ll dp[4][MX];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> line;


    for (int i = 0; i < line.size(); i++)
    {
        if (line[i] == 'l')
            dp[0][i + 1] = dp[0][i] + 1;
        else dp[0][i + 1] = dp[0][i];
    }
    for (int i = 0; i < line.size(); i++)
    {
        if (line[i] == 'o')
            dp[1][i + 1] = dp[0][i] + dp[1][i];
        else dp[1][i + 1] = dp[1][i];
    }
    for (int i = 0; i < line.size(); i++)
    {
        if (line[i] == 'v')
            dp[2][i + 1] = dp[1][i] + dp[2][i];
        else dp[2][i + 1] = dp[2][i];
    }
    for (int i = 0; i < line.size(); i++)
    {
        if (line[i] == 'e')
            dp[3][i + 1] = dp[2][i] + dp[3][i];
        else dp[3][i + 1] = dp[3][i];
    }

    // debug
//    for (int i = 0; i < 4; i++)
//    {
//        for (int j = 0; j <= line.size(); j++)
//        {
//            cout << dp[i][j] << " ";
//        }
//        cout << endl;
//    }


    cout << dp[3][line.size()] << endl;
}