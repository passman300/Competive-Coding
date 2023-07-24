#include <bits/stdc++.h>
using namespace std;

int N;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> N;
    long long ans = 0;
    for (int i = 0; i * 2 <= N; i++) {
        int j = N - i * 2;
        long long temp = 1LL * i * j * (j - 1) / 2;
        if (ans < temp){
            ans = temp;
        };
    }

    cout << ans << endl;
}

