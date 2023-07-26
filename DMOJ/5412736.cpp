#include<bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
const int MX = 3001;

int dp[MX][MX];


int S;
int main() {
    iostream::sync_with_stdio(0);
    cin.tie(0);

    cin >> S;

    int templateMetal[S + 1][S + 1];
    int dp[S + 1][S + 1];

    for (int i = 0; i <= S; i++)
    {
        for (int j = 0; j <= S; j++)
        {
            dp[i][j] = 0;
            templateMetal[i][j] = 0;
        }
    }


    for (int i = 1; i <= S; i++)
    {
        for (int j = 1 ; j <= S; j++)
        {
            cin >> templateMetal[i][j];
        }
    }

    int cnt = 0;
    int maxSize = 0;
    for (int i = 1; i <= S; i++)
    {
        for (int j = 1; j <= S; j++)
        {
            if (templateMetal[i][j] == 1)
            {
                dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
            }
            else
                dp[i][j] = 0;

            if (dp[i][j] > maxSize)
            {
                maxSize = dp[i][j];
                cnt = 0;
            }
            if (dp[i][j] == maxSize) cnt++;
        }
    }

//    for (int i = 1; i <= S; i++)
//    {
//        for (int j = 1 ; j <= S; j++)
//        {
//            cout << dp[i][j] << " ";
//        }
//        cout << endl;
//    }
//
//    cout << cnt << ": " << maxSize << endl;
    cout << cnt * maxSize;
}