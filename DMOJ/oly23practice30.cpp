// Red Black Path
// By Colin Wang
// AK
// Idea: Flood fill/dfs

#include <bits/stdc++.h>
#pragma GCC optimize("Ofast,unroll-loops")
#pragma GCC target("avx2")
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int MAX = 402;


int grid[MAX][MAX];
bool vis[MAX][MAX];
vector<pii> dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
int R, C;
ll ans;

bool inRange(int x, int y){
    return (x > 0 && x <= R && y > 0 && y <= C);
}

void dfs(int a, int b){
    ll q = 0, r = 0;
    stack<pii> s;

    s.push({a, b});
    vis[a][b] = true;

    while(!s.empty()){
        int x = s.top().first;
        int y = s.top().second;

        s.pop();
        if ((x + y) % 2 == 0) q++;
        else r++;

        for (int i = 0; i < 4; i++){
            int nx = x + dir[i].first;
            int ny = y + dir[i].second;

            if (grid[x][y] != grid[nx][ny] && inRange(nx, ny) && !vis[nx][ny]){
                s.push({nx, ny});
                vis[nx][ny] = true;
            }
        }
    }
    ans += q * r;
}

signed main() {

    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> R >> C;
    vector<pii> indexs;


    for (int i = 1; i <= R; i++){
        for (int j = 1; j <= C; j++){
            char temp;
            cin >> temp;
            if (temp == '.'){
                grid[i][j] = 0;
                indexs.push_back({i, j});
            }
            else grid[i][j] = 1;
        }
    }


    for (auto x: indexs){
        int i = x.first;
        int j = x.second;
        dfs(i, j);
    }

    cout << ans;





}
