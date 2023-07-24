#include <bits/stdc++.h>
using namespace std;

long long N;
long long ans = 0;

// long long fun(long long N){
//     long long temp;
//     for (long long i = 1; i <= N; i++)
//     {
//         long long point = N - i + 1;
//         temp += abs(point - i);
//     }
//     return temp;
// }

long long fun2(long long N)
{
    long long temp;

    temp = (2 * N * N) + pow(-1, N) - 1;
    temp = temp / 4;

    long long round(temp);
    return temp;
}

long long fun3(long long N)
{
    long long temp;

    temp = (N * N) / 2;

    return temp;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0),cout.tie(0);

    cin >> N;
    cout << fun3(N) << endl;

    // for (long long i = 10000000; i < 1000000000; i++)
    // {
    //     cout << fun2(i) << ", ";
    // }
    


    // sum of N consective intergers

}


