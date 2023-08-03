#include <bits/stdc++.h>
using namespace std;

const int INF = 1000005;

int maxCal, N;

int dp[INF];

int main() {
    cin.sync_with_stdio(0); cin.tie(0);

    cin >> maxCal >> N;

    vector<int> cals;

    dp[0] = 1;

    for (int i = 0; i < N; i++) {
        int cal;
        cin >> cal;

        for (int j = maxCal - 1; j >= cal; j--){
            dp[j] |= dp[j - cal];
        }
    }

    while(!dp[maxCal] && maxCal > 0){
        maxCal--;
    }

//    for (int i = 0; i < N; i++) {
//        cout << dp[i] << " ";
//    }
//    cout << "\n";

    cout << maxCal << "\n";

}
