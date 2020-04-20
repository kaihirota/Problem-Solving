// C++ program to compute Binomial Probability
#include <iostream>
#include <cmath>
#define thres 92233720368L
typedef long long ll;

using namespace std;
// function to calculate nCr i.e., number of
// ways to choose r out of n objects
double getProb(int n,int k){
    ll count = 0;
    ll cur = 1;
    count += cur;
    int left = n;
    for (int i=0;i<k;++i) {
        cur = cur * (n - i) / (i+1);
        count += cur;
        while (cur > thres) {
            count /= 2;
            cur /= 2;
            --left;
        }
    }
    double res = count;
    while (left--) res /= 2;
    return res;
}

int main() {
    int T;
    cin >> T;
    int W, H, L, U, R, D;
    for (int t=1;t<=T;++t) {
        double res = 0.0;
        cin >> W >> H >> L >> U >> R >> D;
        if (R < W && U > 1)
            res += getProb(R + U-2, U-2);
        if (D < H && L > 1)
            res += getProb(D +L-2, L-2);
        cout << "Case #" << t << ": " << res << endl;
    }
}
