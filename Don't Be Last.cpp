#include <bits/stdc++.h>
using namespace std;


int N;
string letters;

int main(){
    cin >> N;


    cin >> letters;

    for (int i = 1; i <= N; i++){
        unordered_map<string, int> mails;
        bool f = false;
        string substring;
        for (int j = 0; j <= N - i; j++){
            substring = letters.substr(j, i);
            mails[substring]++;
        }


        for (auto [s, i]: mails){
            if (mails[substring] > 1){
                f = true;
            }
        }

        if (!f) {cout << i << endl; break;}
    }

    return 0;

}