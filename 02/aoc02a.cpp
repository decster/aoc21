#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
    char cmd[128];
    int v;
    int x = 0, y = 0;
    while (scanf("%s %d\n", cmd, &v) == 2) {
        if (strcmp("forward", cmd)==0) {
            x += v;
        } else if (strcmp("down", cmd)==0) {
            y+=v;
        } else if (strcmp("up", cmd) ==0) {
            y = std::max(0, y-v);
        }
    }
    printf("%d\n", x*y);
    return 0;
}
