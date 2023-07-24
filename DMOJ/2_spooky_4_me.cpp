#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
// #define int long long

int N, L, S;
int a, b, s;
long long ans;

map<int, int> houses;


signed main(){
    ios::sync_with_stdio(false);
    cin.tie(0); 

    cin >> N >> L >> S;

    for (int i = 0; i < N; i++) {
        cin >> a >> b >> s;
        houses[a] += s;
        houses[b + 1] -= s;
    }

    int x = 0;
    int y  = 0;


    for (auto &k : houses) {
        k.second = k.second + x;
        if (x < S) {
            ans += k.first - y;
        }
        x = k.second;
        y = k.first;
    }

    if (abs(houses.end()->second) < S) {
        ans += L - y;
    }

    cout << ans << endl;

    
}

