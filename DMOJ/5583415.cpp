#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;


int R, C;
int g[1003][1001];
int cnt = 0;


void dfs(int r, int c){
    g[r][c] = 0;
    if(r-1 >= 0 && g[r-1][c] != 0) dfs(r-1, c);
    if(c-1 >= 0 && g[r][c-1] != 0) dfs(r, c-1);
    if(r+1 < R && g[r+1][c] != 0) dfs(r+1, c);
    if(c+1 < C && g[r][c+1] != 0) dfs(r, c+1);


    if(r-1 >= 0 && c-1 >= 0 && g[r-1][c-1] != 0) dfs(r-1, c-1);
    if(r-1 >= 0 && c+1 < C && g[r-1][c+1] != 0) dfs(r-1, c+1);
    if(r+1 < R && c-1 >= 0 && g[r+1][c-1] != 0) dfs(r+1, c-1);
    if(r+1 < R && c+1 < C && g[r+1][c+1] != 0) dfs(r+1, c+1);

}


int main(){
    ios::sync_with_stdio(0); cin.tie(0);


    cin >> R >> C;
    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++)
            cin >> g[i][j];
    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++)
            if(g[i][j] > 0){ cnt++; dfs(i, j); }
    cout << cnt << "\n";


}