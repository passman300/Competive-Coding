#include <iostream>
using namespace std;
typedef pair<int, int> pii;
const int MX = 1000l;

int main() {
    iostream::sync_with_stdio(0);
    cin.tie(0);

    int H, S, Q;

    cin >> H;
    cin >> S;
    cin >> Q;

    while (Q--)
    {
        H -= S;
        cout << H << endl;
    }


}