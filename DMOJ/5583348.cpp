#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int N;
vector<int> ans;

int main(){
    ios::sync_with_stdio(0); cin.tie(0);

    cin >> N;

//    cout << N / 2 << '\n';

    for (int i = 0; i < N; i++){
        vector<int> nums;

        for (int j = 0; j < N; j++){
            int a;
            cin >> a;

            nums.push_back(a);
        }

        sort(nums.begin(), nums.end());
        int x = nums[N / 2];

        ans.push_back(x);

    }

    sort(ans.begin(), ans.end());

    cout << ans[N / 2] << '\n';
}