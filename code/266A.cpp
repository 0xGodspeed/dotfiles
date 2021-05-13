#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int k, n, w;
    cin >> k >> n >> w;
    int ans = (k*w*(w+1)/2); 
    if (n > ans) {
        cout << 0;
    }
    else {
        cout << ans - n;
    }
}
