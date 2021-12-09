#include <stdio.h>
#include <string.h>
#include <vector>
#include <string>
#include <stdint.h>
using namespace std;

int main(int argc, char **argv) {
    vector<string> all;
    char t[128];
    while (scanf("%s\n", t) == 1) {
        all.push_back(t);
    }
    int W = all[0].size();
    vector<int> idxes;
    for (size_t i=0;i<all.size();i++) {
        idxes.push_back(i);
    }
    for (size_t i=0;i<W;i++) {
        int cnt = 0;
        for (auto idx : idxes) {
            if (all[idx][i]=='1') {
                cnt++;
            }
        }
        vector<int> newidxs;
        if (cnt >= all.size()/2) {
            for (auto idx : idxes) {
                if (all[idx][i]=='1') {
                    newidxs.push_back(idx);
                }
            }
        } else {
            for (auto idx : idxes) {
                if (all[idx][i]=='0') {
                    newidxs.push_back(idx);
                }
            }
        }
        idxes.swap(newidxs);
    }
    int a = 0;
    for (size_t i=0;i<W;i++) {
        if (all[idxes[0]][i] == '1') {
            a |= (1 << (W-1-i));
        }
    }
    int b = 0;
    for (size_t i=0;i<W;i++) {
        int cnt = 0;
        for (auto idx : idxes) {
            if (all[idx][i]=='1') {
                cnt++;
            }
        }
        vector<int> newidxs;
        if (cnt >= all.size()/2) {
            for (auto idx : idxes) {
                if (all[idx][i]=='0') {
                    newidxs.push_back(idx);
                }
            }
        } else {
            for (auto idx : idxes) {
                if (all[idx][i]=='1') {
                    newidxs.push_back(idx);
                }
            }
        }
        idxes.swap(newidxs);
        if (idxes.size()==1) {
            return
        }
    }

    printf("gamma: %d  eps: %d\n", ret, (((1<<W)-1)^ret));
    printf("%d\n", ret * (((1<<W)-1)^ret));
    return 0;
}
