// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
#define ll long long
using namespace std;
typedef array<int, 3> ar3;
typedef array<int, 4> ar4;
const int MX = 1e7;

int N, R, C;
vector<int> roomSizes;
int ans;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> dirx = {1, 0, 0, -1};
    vector<int> diry = {0, 1, -1, 0};

    cin >> N;
    cin >> R;
    cin >> C;

    char room[R][C];

    for (int r = 0; r < R; r++)
    {
        for (int c = 0; c < C; c++)
        {
            cin >> room[r][c];
        }
    }

    //flood fill
    for (int r = 0; r < R ; r++)
    {
        for (int c = 0; c < C; c++)
        {
            if (room[r][c] == '.')
            {
                queue<pair<int, int>> q;
                room[r][c] = 'I';
                int cnt = 1;
                q.push({r, c});

                while (!q.empty())
                {
                    auto[x, y] = q.front();
                    q.pop();

                    for (int i = 0; i < 4 ; i++)
                    {
                        int newr = dirx[i] + x;
                        int newy = diry[i] + y;

                        if (newr >= 0 && newr < R && newy >= 0 && newy < C)
                        {
                            if (room[newr][newy] == '.')
                            {
                                room[newr][newy] = 'I';
                                q.push({newr, newy});
                                cnt++;
                            }
                        }
                    }
                }
                roomSizes.push_back(cnt);
            }
        }
    }

    sort(roomSizes.begin(), roomSizes.end(), greater());
    for (int i = 0; i < roomSizes.size(); i++)
    {
        if (N - roomSizes[i] >= 0)
        {
            ans++;
            N -= roomSizes[i];
        }
        else break;
    }

    if (ans == 1)
    {
        cout << ans << " room, " << N << " square metre(s) left over" << endl;

    }
    else
    {
        cout << ans << " rooms, " << N << " square metre(s) left over" << endl;

    }
    //2 rooms, 9 square metre(s) left over

}