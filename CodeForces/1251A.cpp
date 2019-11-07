#include <iostream>
//#include <fstream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

//    ifstream cin("input");

    int n;
    string s;


    cin >> n;
    for (int i=0; i<n; i++) {

        bool chk[26] = {false};
        bool app[26] = {false};

        cin >> s;

        app[(int)s[0]-97] = true;
        if (s[0] != s[1]) {
            chk[(int)s[0]-97] = true;
        }

        for (int j = 0; j < s.size(); j++) {
            app[(int)s[j]-97] = true;
            if (j==s.size() || (s[j]!= s[j+1])) {
                chk[(int)s[j]-97] = true;
            } else {
                j++;
            }
        }

        for (int j = 0; j < 26; j++) {
            if (app[j] && chk[j])
                cout << char(j+97);
        }

        cout << endl;
    }

    return 0;
}
