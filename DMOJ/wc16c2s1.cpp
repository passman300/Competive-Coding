#include <bits/stdc++.h>
using namespace std;

const int INF = 1e5 + 3;

int N;
vector<string> equation;

string solveAnd(string a, string b) {
    if (a == "true" && b == "true") return "true";
    if (a == "true" && b == "false") return "false";
    if (a == "false" && b == "true") return "false";
    if (a == "false" && b == "false") return "false";
    if (a == "false" && b == "unknown") return "false";
    if (a == "unknown" && b == "false") return "false";
    if (a == "unknown" && b == "true") return "unknown";
    if (a == "true" && b == "unknown") return "unknown";
    if (a == "unknown" && b == "unknown") return "unknown";
}

string solveOr(string a, string b){
    if (a == "true" && b == "true") return "true";
    if (a == "true" && b == "false") return "true";
    if (a == "false" && b == "true") return "true";
    if (a == "false" && b == "false") return "false";
    if (a == "false" && b == "unknown") return "unknown";
    if (a == "unknown" && b == "false") return "unknown";
    if (a == "unknown" && b == "true") return "true";
    if (a == "true" && b == "unknown") return "true";
    if (a == "unknown" && b == "unknown") return "unknown";
}

void printVec(vector<string> v) {
    for (string s : v) {
        cout << s << " ";
    }
    cout << endl;
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);

    cin >> N;

    vector<int> andIdx;
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        equation.push_back(s);

        if (s == "and"){andIdx.push_back(i);}
    }


    for (int i = 0; i < andIdx.size(); i++){
        string a, b, c;
        int x, y, z;

        x = andIdx[i] - 1 - i*2;
        y = andIdx[i] - i *2;
        z = andIdx[i] + 1 - i*2;

        a = equation[x];
        b = equation[y];
        c = equation[z];

        equation.erase(equation.begin() + x, equation.begin() + x + 3);

        equation.insert(equation.begin() + x, solveAnd(a, c));

//        printVec(equation);
    }

    while (equation.size() > 1){
        string a, b, c;


        a = equation[0];
        b = equation[1];
        c = equation[2];

        equation.erase(equation.begin(), equation.begin() + 3);

        equation.insert(equation.begin(), solveOr(a, c));

//        printVec(equation);
    }
    printVec(equation);





}
