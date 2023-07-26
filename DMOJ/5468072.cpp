#include <bits/stdc++.h>
using namespace std;
typedef array<int, 3> arr;
typedef long long ll;
const int MX = 1e5 + 5;

int N;
vector<string> ans;

bool cmp(string s1, string s2)
{
    if (s1.size() == s2.size()) {
        return s1 < s2;
    }
    else
    {
        return s1.size() < s2.size();
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        string line;
        cin >> line;

        string num = "";
        bool flag = false;
        for (int j = 0; j < line.size(); j++)
        {

            if (isdigit(line[j]))
            {
                flag = true;
                num += line[j];
            }
            else
            {
                if (flag)
                {
                    int temp = 0;
                    for (int k = 0; k < num.size() - 1; k++)
                    {
                        if (num[k] == '0') temp++;
                        else break;
                    }
                    ans.push_back(num.substr(temp, num.size() - temp));
                }
                flag = false;
                num = "";
            }
        }

        if (flag)
        {
            int temp = 0;
            for (int k = 0; k < num.size() - 1; k++)
            {
                if (num[k] == '0') temp++;
                else break;
            }
            ans.push_back(num.substr(temp, num.size() - temp));
        }


    }

    sort(ans.begin(), ans.end(), cmp);
    for (string i: ans) cout << i << '\n';
}