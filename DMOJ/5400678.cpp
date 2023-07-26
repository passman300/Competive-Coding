#include <bits/stdc++.h>
#define ll long long
using namespace std;
typedef array<int, 4> arr;
const int MX = 1002;


int cards[5];
int N, M;
int ans = -INT32_MAX;

int solve(int a, int b, int c, int d)
{
    int points = 0;

    a = cards[1] + a;
    b = cards[2] + b;
    c = cards[3] + c;
    d = cards[4] + d;

    points += a * a + b * b + c * c + d * d;

    int lowMin = INT32_MAX;
    lowMin = min(lowMin, a);
    lowMin = min(lowMin, b / 2);
    lowMin = min(lowMin, c / 2);
    lowMin = min(lowMin, d);

    points += lowMin * 7;

//    printf("%d %d %d %d %d\n", a, b, c, d, points);
    return points;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        char temp;
        cin >> temp;
        if (temp == 'd') cards[1]++;
        if (temp == 'k') cards[2]++;
        if (temp == 'o') cards[3]++;
        if (temp == 'r') cards[4]++;
    }

    for (int a = 0; a <= M; a++)
    {
        for (int b = 0; b <= M; b++)
        {
            for (int c = 0; c <= M; c++)
            {
                for (int d = 0; d <= M; d++)
                {
                    if (a + b + c + d <= M)
                    {
                        ans = max(ans, solve(a, b, c, d));
                    }
                }
            }
        }
    }

    cout << ans;
}