#include <bits/stdc++.h>
using namespace std;

int N, X;
vector<int> nums;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0),cout.tie(0);

    cin >> N >> X;

    if (N % 2 != X % 2){
        cout << -1 << '\n';
        return 0;
    }

    int numOut = N - X;

    for (int i = 1; i <= N; i++){
        int temp = i * 2;

        if (i % 2 == 0 && i <= numOut){
            nums.emplace_back(temp - 1);
        }
        else{
            nums.emplace_back(temp);
        }
    }
    

    for (int i = 0; i < nums.size() - 1; i++){
        cout << nums[i] << " ";
    } cout << nums[nums.size() - 1] << '\n';

    

}