#include <bits/stdc++.h>
using namespace std;


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    float a, b;
    float n;
    cin >> a >> b;
    if (a == b) {
        n = 1;
    }
    else {
        n = log(b/a)/0.4054;
    }
    cout << ceil(n);
}