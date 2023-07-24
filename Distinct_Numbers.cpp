#include <bits/stdc++.h>
using namespace std;



int main(){

    int N;
    set<int> nums;

    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);


    cin >> N;
    int temp;
    for (int i = 0 ; i < N; i++){
        cin >> temp;
        nums.insert(temp);
    }

    cout << nums.size() << endl;
    return 0;
}