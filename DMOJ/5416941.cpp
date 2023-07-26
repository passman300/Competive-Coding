#include <bits/stdc++.h>
using namespace std;
const int MM = 1003;

int D, I, R;
string a;
string b;
int dp[MM][MM];

int main(){
    cin.sync_with_stdio(0);
    cin.tie(0);

    cin >> D >> I >> R;

    cin >> a >> b;

    for (int i = 0; i <= a.size(); i++)
    {
        for (int j = 0; j <= b.size(); j++)
        {
            if (j == 0 && i == 0) continue;
            if (j == 0 && i != 0)
            {
                dp[i][j] = dp[i - 1][j] + D;
            }
            else if (i == 0 && j != 0)
            {
                dp[i][j] = dp[i][j - 1] + I;
            }

            else if (a[i - 1] == b[j - 1] && i != 0 && j != 0)
            {
                dp[i][j] = dp[i - 1][j - 1];
            }
            else
            {
                int del, ins, rep;

                del = dp[i - 1][j] + D;
                ins = dp[i][j - 1] + I;
                rep = dp[i - 1][j - 1] + R;

                dp[i][j] = min(min(del, ins), rep);
            }

        }
    }

    cout << dp[a.size()][b.size()];
}