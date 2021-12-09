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
    int ret = 0;
    for (size_t i=0;i<W;i++) {
        int cnt = 0;
        for (size_t j=0;j<all.size();j++) {
            if (all[j][i]=='1') {
                cnt++;
            }
        }
        if (cnt > all.size()/2) {
            ret |= (1 << (W-1-i));
        } else if (cnt == all.size()/2) {
            printf("error\n");
        }
    }
    printf("gamma: %d  eps: %d\n", ret, (((1<<W)-1)^ret));
    printf("%d\n", ret * (((1<<W)-1)^ret));
    return 0;
}

