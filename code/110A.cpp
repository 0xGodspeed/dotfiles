#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll n;
    int temp=0;
    int ans=0;
    cin >> n;
    do {
       temp = n%10;
       n = n/10;
       if (temp == 4 || temp ==7) {
           ans++;
       }
    }
    while (n);
    if (ans == 7 || ans == 4) {
        cout << "YES";
    } else {
        cout << "NO";
    }
}

