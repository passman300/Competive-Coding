#include <bits/stdc++.h>
using namespace std;
typedef array<int, 3> arr;
const int MX = 1e5 + 5;

int N;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    while(N--)
    {
        string s;
        cin >> s;

        int cnt = 0;
        bool flag = true;
        vector<char> s_final;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == '(')
            {
                cnt++;
            }
            else if (s[i] == ')')
            {
                cnt--;
            }

            if (cnt < 0) {
                flag = false;
                break;
            }
        }
        if (cnt != 0)
        {
            flag = false;
        }


        if (flag)
        {
            cout << "YES" << endl;
        }
        else {cout << "NO" << endl;}


    }


}