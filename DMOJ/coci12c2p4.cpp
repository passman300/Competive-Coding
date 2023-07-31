#include <bits/stdc++.h>
using namespace std;
typedef array<int, 3> arr3;

const long long MAX_VALUE = 1e18;
int N;
multiset<int> notUsed;
multiset<int> secondCaseDiff; // mutisets sort themselves :)
vector<pair<int, int>> meals;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    for (int i = 0; i < N; i++){
        int a, b;

        cin >> a >> b;
        meals.emplace_back(b, -a);
        notUsed.emplace(a);
    }

    sort(meals.begin(), meals.end());

//    for (int i = 0; i < N; i++){
//        secondCaseDiff.emplace(meals[i].second - meals[i].first);
//    }

    long long sum = 0;
    for (int K = 1; K <= N; K++){
        long long ans = MAX_VALUE;

        if (K > 1){
            auto temp = notUsed.find(abs(meals[K - 2].second));
            notUsed.erase(temp);
        }
        ans = min(ans, sum + *notUsed.begin());
//        cout << *notUsed.begin() << "\n";

        sum += meals[K-1].first;

        secondCaseDiff.emplace(abs(meals[K-1].second)- meals[K-1].first);
        ans = min(ans, sum + *secondCaseDiff.begin());

        cout << ans << "\n";
    }
}


