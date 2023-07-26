#include <bits/stdc++.h>
using namespace std;
const int MM = 3002;
string a,b;

int dp[MM][MM];

int main(){
//cin >> N >> M;
    cin>>a>>b;
    for(int i=1; i<=a.length(); i++) {
        for(int j=1; j<=b.length(); j++){
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            if(a[i - 1] == b[j - 1]) {
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1);
            }
        }
    }

    // for (int i = 0; i <= a.length(); i++)
    // {
    //     for (int j = 0; j <= b.length(); j++)
    //     {
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    string ans;
    int x = a.length();
    int y = b.length();
    while(x != 0 && y != 0){
        if(dp[x][y] == dp[x-1][y]){
            x--;
        }
        else if(dp[x][y] == dp[x][y-1]){
            y--;
        }
        else{
            ans = a[x-1] + ans;
            x--;
            y--;
        }
    }
//    reverse(ans.begin(), ans.end());
    cout<<ans;

    // cout<<create(dp, a, b, a.length(), b.length());

}