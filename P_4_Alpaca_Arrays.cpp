#include <bits/stdc++.h>
using namespace std;


int N, Q;
int l, r, x;

vector<int> nums;
vector<int> mutiPSA;

void printVec(vector<int> vec){
    for (int x: vec){
        cout << x << " ";
    } cout << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0),cout.tie(0);

    cin >> N >> Q;

    for (int i = 0; i < N; i++){
        int temp;
        cin >> temp;

        nums.push_back(temp);
    }

    mutiPSA.push_back(nums[0]);
    for (int i = 1; i < N; i++){
        mutiPSA.push_back(mutiPSA[i - 1] * nums[i]);
    }

    
    // for (int temp: mutiPSA)
    // {
    //     cout << temp << " ";
    // } cout << endl;

    for (int i = 0; i < Q; i++){
        cin >> l >> r >> x;
        string ans = "NO";

        int value = mutiPSA[r] - mutiPSA[l - 1];

        if (value % x == 0){ ans = "YES";}

        cout << ans << endl;
        
    }
    return 0;
}


