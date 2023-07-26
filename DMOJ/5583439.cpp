#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int MOD = 1e9 + 7;
const int MAX = 1e5 + 5;



int N, K;
int psa[MAX];


int main(){
    ios::sync_with_stdio(0); cin.tie(0);


    cin >> N >> K;

    for (int i = 1; i <= N; i++) {
        if (i <= K + 1) {
            psa[i] = 1;
        }
        else {
            int temp = ((((psa[i - K - 1] + 1) % MOD) + MOD ) % MOD);
            psa[i] = temp;
        }
        int temp = ((((psa[i - 1] + psa[i]) % MOD) + MOD ) % MOD);
        psa[i] = temp;
    }


    cout << ((((psa[N] + 1) % MOD) + MOD ) % MOD);

}