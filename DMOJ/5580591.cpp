#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;
typedef pair<int, int> pii;

int N;
int ans;

int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    cin >> N;

    for (int i = 0; i < N; i++){
        int a, b;
        cin >> a >> b;

        if (a > b) {ans++;}

    }

    cout << ans << endl;

    return 0;


}