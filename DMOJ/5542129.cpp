#include <bits/stdc++.h>
using namespace std;


int N, M;


int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    cin >> N >> M;

    char table[N][M];

    fill(table[0], table[0] + N * M, '.');


    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            char x;
            cin >> x;

            if (x == '#')
            {
                table[i][j] = '#';
                table[i][j + 1] = '#';
                table[i + 1][j] = '#';
                table[i + 1][j + 1] = '#';
            }
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cout << table[i][j];
        }
        cout << endl;
    }
}