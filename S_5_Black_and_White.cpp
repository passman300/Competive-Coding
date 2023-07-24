#include <bits/stdc++.h>
using namespace std;

int N; // board size
int M;

int x, y, w, h;

bool board[10001][10001];





int main(){
    ios::sync_with_stdio(NULL);
    cin.tie(0);
    int cnt = 0;

    cin >> N >> M;

    for (int i = 0; i < M; i++){
        cin >> x >> y >> w >> h;

        for (int a = x; a < x + w; a++){
            for (int b = y; b < y + h; b++){
                board[a][b] = !board[a][b];

                if (board[a][b] == 1){
                    cnt++;
                }
                else{
                    cnt--;
                }

            }
        }
    }

    // int cnt = 0;
    // for (int a = 0; a < N; a++){
    //     for (int b = 0; b < N; b++){
    //         // cout << board[a][b];
    //         if (board[a][b] == 1) {cnt++;}
    //     }
    // }

    cout << cnt << endl;
}