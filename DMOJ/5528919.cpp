#include <bits/stdc++.h>
using namespace std;
#define endl '\n';
typedef long long ll;
typedef pair<int, int> pii;
const int MX = 32;
const int MOD = 1e6;



vector<int> ans;
multiset<int> freq;
int N, M;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;

    for (int i = 0 ; i < N; i++)
    {
        int x;
        cin >> x;
        freq.insert(x);
    }

    ans.push_back(*freq.begin());
    freq.erase(freq.begin());

    for (int i = 1; i < N; i++)
    {
        auto it = freq.lower_bound(M - ans.back());
        if (it == freq.end())
        {
            cout << -1 << endl;
            return 0;
        }
        else
        {
            ans.push_back(*it);
            freq.erase(it);
        }
    }

    for (auto i: ans)
    {
        cout << i << " ";
    }

}