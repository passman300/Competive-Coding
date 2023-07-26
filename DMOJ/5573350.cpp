#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

//int R, C;
//vector<int> validMask;
//vector<int> lst[3000];
//long long dp[100][3000];

int R, C; vector<int> validMask, lst[3000]; long long ans, dp[100][4000];


int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(false);


//    cout << "test" << endl;
    cin >> R >> C;
    // to check if two bits are beside each other (x & x >> 1) == 0, since u shift one bit to the right
    // check if two bits are one 0 between them (x & x >> 2) == 0, since u shift two bits to the right
    for (int mask = 0; mask < 1 << C - 2; mask++) { // hardcoded all 22 chases --> result in 599186 mask
        if ((mask & mask >> 1) == 0 && (mask & mask >> 2) == 0) {
//            cout << mask << '\n';
            validMask.push_back(mask);
        }
    }

//    cout << validMask.size() << '\n';


    for (int i = 0; i < validMask.size(); i++) {
//        list[i] = validMask[i];
        dp[1][i] = 1;
        for (int j = 0; j < validMask.size(); j++){
            int x = validMask[j];
            int y = validMask[i];
            if (((x | x >> 1 | x << 1) & y ) == 0 ) lst[i].push_back(j);

        }
    }

    for (int i = 2; i < R; i++) {
        for (int j = 0; j < validMask.size(); j++){
            for (int k : lst[j]){
                dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD;
            }
        }
    }

//    long long ans = 0;
    for (int i = 0; i < validMask.size(); i++) {
        ans = (ans + dp[R - 1][i]) % MOD;
    }
    cout << (ans - 1 + MOD) % MOD << '\n';
//    return 0;




}