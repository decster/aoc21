#include <stdio.h>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
    vector<int> all;
    vector<int> sum;
    int next;
    int ret = 0;
    while (scanf("%d", &next) == 1) {
        all.push_back(next);
        if (all.size() >= 3) {
            sum.push_back(all[all.size()-1] + all[all.size()-2] + all[all.size()-3]);
        }
        if (sum.size() > 1 && sum[sum.size()-1] > sum[sum.size()-2] > 0) {
            ret++;
        }
    }
    printf("%d\n", ret);
    return 0;
}
