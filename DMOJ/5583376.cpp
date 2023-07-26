#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int N;
vector<int> nums;

int main(){
    ios::sync_with_stdio(0); cin.tie(0);

    cin >> N;

    for (int i = 0 ; i < N; i++)
    {
        int x; cin >> x;
        nums.push_back(x);
    }

    int ans = 0;
    int s = 0;
    int e = 0;
    for (int i = 0; i < N; i++){
        if (i == 0) continue;

        if (nums[i] <= nums[i - 1]){
            e++;
        } else{
//            cout << s << " " << e << endl;
            ans = max(ans, e - s + 1);
            s = i;
            e = i;
        }
    }
    ans = max(ans, e - s + 1);

    cout << ans;

}