#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;

map<pii, int> regCords;
map<int, int> xCords;
map<int, int> yCords;

int N, Q;
int a, x, y;
char b;
int c;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0),cout.tie(0);

    cin >> N >> Q;

    for (int i = 0 ; i < N; i++){
        cin >> x >> y;
        regCords[{x, y}] = 1;
        xCords[x]++;
        yCords[y]++;
    }

    for (int i = 0; i < Q; i++)
    {
        cin >> a;

        if (a == 1){
            cin >> x;
            cin >> y;

            if (regCords[{x, y}] == 1) {cout << "salty" << endl;}
            else {cout << "bland" << endl;}
        }
        else{
            cin >> b >> c;
            if (b == 'X') {cout << xCords[c] << endl;}
            else {cout << yCords[c] << endl;}
        }
    }

}