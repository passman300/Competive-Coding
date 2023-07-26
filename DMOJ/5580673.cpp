#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e5 * 2 + 5;
const int MOD = 1e9 + 7;
typedef pair<int, int> pii;

int N;
vector <int> adj[MAX];
int vis[MAX];



int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    queue <int> q;

    for (int course = 0; course < N; course++)
    {
        int i;
        cin >> i;

        if (i == 0)
        {
            q.push(course);
        }
        else
        {
            for (int j = 0; j < i; j++)
            {
                int x;
                cin >> x;

                adj[x-1].push_back(course);
                vis[course]++;
            }
        }
    }

    while(!q.empty())
    {
        int cur = q.front();
        q.pop();

        cout << cur + 1 << " ";

        for (int K : adj[cur])
        {
            vis[K]--;
            if (vis[K] == 0)
            {
                vis[K] = -1;
                q.push(K);
            }
        }

    }


}