#include <iostream>
//#include <fstream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

//    ifstream cin("input");

    int n;
    cin >> n;

    for (int i=0; i<n; i++) {

        int m;
        cin >> m;

        vector<int> l;
        int one = 0;
        int zero = 0;
        int result = 0;
        int taboo = 0;


        for (int j = 0; j < m; j++) {
            string s;
            cin >> s;

            if (s.size() % 2 != 0) {
                result++;
                taboo  += s.size();
                continue;
            }

            l.push_back(s.size());

            for (int k = 0; k <s.size(); k++) {
                if (s[k] == '0')
                    zero++;
                else
                    one++;
            }
        }


        sort(l.begin(), l.end());


        for (int x : l) {
            int mid = int(x / 2);

            if (mid % 2 != 0)
                if (zero > one)
                    mid++;
                else
                    mid--;

            if (zero>=one) {
                while (zero >= mid + 2)
                    mid += 2;
            } else {
                while (one >= x - mid + 2 && mid - 2 >= 0)
                    mid -=2;
            }

            if (zero >= mid && one >= x-mid) {
                zero -= mid;
                one -= x-mid;
                result++;
            } else if (zero < mid && one < x-mid && taboo >= mid-zero+x-mid-one) {
                taboo -= mid-zero+x-mid-one;
                zero -= mid;
                one -= x-mid;
                result++;
            } else if (zero < mid && taboo >= mid-zero) {
                zero -= mid;
                one -= x-mid;
                taboo -= mid-zero;
                result++;
            } else if (one < x-mid && taboo >= x-mid-one) {
                zero -= mid;
                one -= x-mid;
                taboo -= x-mid-one;
                result++;
            } else
                break;
        }

        cout << result << endl;
    }

    return 0;
}
