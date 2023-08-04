#include <bits/stdc++.h>
using namespace std;

const int INF = 1e5 + 3;

int houses, roads, errands, c;

vector<int> adj[INF];
int dist[INF];

int main() {
    cin.sync_with_stdio(0); cin.tie(0);

    cin >> houses >> roads >> errands >> c;

    for (int i = 0; i < roads; i++){
        int a, b;

        cin >> a >> b;

        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    for (int i = 0; i < INF; i++) {dist[i] = -1;}

    queue<int> q;
    q.push(c);

    dist[c] = 0;

    while(!q.empty()){
        int u = q.front();
        q.pop();

        for (int v : adj[u]){
            if (dist[v] == -1){
                dist[v] = dist[u] + 1;
                
                q.push(v);
            }
            if ((dist[u] + 1) < dist[v]){
                dist[v] = dist[u] + 1;
                
                q.push(v);
            }
        }
    }

    // for (int i = 0; i < 8; i++){
    //     cout << dist[i] << " ";
    // }
    // cout << endl;


    for (int i = 0; i < errands; i++){
        int u, v;
        cin >> u >> v;

        int a, b;
        a = dist[u];
        b = dist[v];

        if (a == -1 || b == -1){
            cout << "This is a scam!" << endl;
        } else {
            cout << a + b << endl;
        }

    }



}
