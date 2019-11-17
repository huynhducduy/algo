using namespace std;

#include "iostream"
#include "fstream"

int n, m, pa[(int)2e5+1], ans;

int find(int u) {
    pa[u] = pa[u] == u ? u : find(pa[u]);
    return pa[u];
}

void merge(int x, int y) {
    int X = find(x), Y = find(y);
    if (X > Y) swap(X,Y);
    pa[X] = Y;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

//    ifstream cin("input");

    cin >> n >> m;

    for (int i = 1; i <= n; i++) pa[i]=i;

    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        if (find(x) != find(y))
            merge(x,y);
    }

    for (int i = 1; i <= n; i = find(i)+1)
        for (int j = i+1; j <= find(i); j++) {
            if (find(i) != find(j)) {
                ans++;
                merge(i, j);
            }
        }

    cout << ans << endl;
    return 0;
}
