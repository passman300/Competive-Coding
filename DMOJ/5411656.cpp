#include <iostream>
using namespace std;
typedef pair<int, int> pii;
const int MX = 3001;

int dp[MX][MX];

int main() {
    iostream::sync_with_stdio(0);
    cin.tie(0);

    string a;
    string b;

    cin >> a;
    cin >> b;

    for (int i = 0 ; i <= a.size(); i++)
    {
        dp[i][0] = 0;
    }
    for (int j = 0; j <= b.size(); j++)
    {
        dp[j][0] = 0;
    }


    for (int i = 1; i <= a.size(); i++)
    {
        for (int j = 1; j <= b.size(); j++)
        {
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);

            if (a[i - 1] == b[j - 1])
            {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1);
            }
        }
    }


//    // print table
//    for (int i = 0; i <= a.size(); i++)
//    {
//        for (int j = 0; j <= b.size(); j++)
//        {
////            cout << dp[i][j] << " ";
//        }
////        cout << endl;
//    }

    string ans = "";

    int i = a.size();
    int j = b.size();

    while (true)
    {
        if (i > 0 && j > 0)
        {
            if (a[i - 1] == b[j - 1])
            {
                ans = a[i - 1] + ans;

                i--;
                j--;
            }
            else if (dp[i][j - 1] > dp[i - 1][j])
            {
                j --;
            }
            else i --;
        }
        else break;
    }

    cout << ans;



}