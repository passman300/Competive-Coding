#include <bits/stdc++.h>
using namespace std;
const int MM = 1003;
string a,b;


int N;
vector<pair<int, char>> geese;
vector<pair<int, char>> hawks;
int dp[MM][MM];

int main(){
    cin.sync_with_stdio(0);
    cin.tie(0);

    cin >> N;

    string a;
    cin >> a;
    for (int i = 0; i < N; i++)
    {
        char WL;
        int score;
        WL = a[i];
        cin >> score;


        geese.push_back({score, WL});
    }

    string b;
    cin >> b;
    for (int i = 0; i < N; i++)
    {
        char WL;
        int score;
        WL = b[i];
        cin >> score;

        hawks.push_back({score, WL});
    }


    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);

            if ((hawks[i - 1].second == 'W' && geese[j - 1].second == 'L' && hawks[i - 1].first > geese[j - 1].first) ||
            (hawks[i - 1].second == 'L' && geese[j - 1].second == 'W' && hawks[i - 1].first < geese[j - 1].first))
            {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + hawks[i - 1].first + geese[j - 1].first );
            }
        }
    }

    cout << dp[N][N];

}