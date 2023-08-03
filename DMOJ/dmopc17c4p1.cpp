#include <bits/stdc++.h>
using namespace std;

int N, Q;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);

    cin >> N >> Q;

    int rib[N];

    memset(rib, 0, sizeof rib);

    for (int i = 0; i < Q; i++){
        int a, b;

        cin >> a >> b;

        rib[a]++;
        rib[b]--;
//        for (int j = a; j < b; j++){
//            rib[j] = 1;
//        }
    }

    int purple = 0;
    int blue = 0;

    int cur = 0;
    for (int i = 0; i < N; i++){
        cur += rib[i];
        if (cur){
            blue++;
        }else{
            purple++;
        }
    }
    cout << purple << ' ' << blue;
}
