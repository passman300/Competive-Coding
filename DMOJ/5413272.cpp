#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pii;
//const int MX = 1e14 + 3;

vector<pii> days;

ll N, T;
signed main() {
    iostream::sync_with_stdio(0);
    cin.tie(0);


    cin >> N >> T;
    for (int i = 0 ; i < N ; i++)
    {
        ll a, b;
        cin >> a >> b;
        days.emplace_back(a, b);
    }


    ll leftOver = 0;
    ll eatenCnt = 0;
    for (ll i = 0; i < N - 1; i++) {
        auto[day, hay] = days[i];

        ll nextDay = days[i + 1].first;

        if ((nextDay - day) >= hay)
        {
            eatenCnt += hay;
        }
        else
        {
            eatenCnt += nextDay - day;
            days[i + 1].second += hay - (nextDay - day);
        }
    }


    auto[day, hay] = days[N - 1];
    ll totalDays = T - day + 1;
    eatenCnt += min(totalDays, hay);

    cout << eatenCnt;
}