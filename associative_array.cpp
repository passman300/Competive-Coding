#include <bits/stdc++.h>
using namespace std;


int N;
unordered_map<int, int> nums;

int main(){
    cin >> N;


    int a, b, c;
    for (int i = 0; i < N; i++)
    {
        cin >> a;

        if (a) {
            cin >> b >> c;
            nums[b] = c;
        }
        else {
            cin >> b;
            cout << nums[b] << endl;
        }
    


    }
}