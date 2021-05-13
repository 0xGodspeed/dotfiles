#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    float a, b;
    cin >> t;
    while (t--) {
        cin >> a >> b;
        cout << b*ceil(a/b)-a << scientific << '\n'; 
    }
}

