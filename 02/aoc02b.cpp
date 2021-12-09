#include <stdio.h>
#include <string.h>
#include <vector>
#include <stdint.h>
using namespace std;

int main(int argc, char **argv) {
    char cmd[128];
    int v;
    int x = 0, y = 0, aim=0;
    while (scanf("%s %d\n", cmd, &v) == 2) {
        if (strcmp("forward", cmd)==0) {
            x += v;
            y = max(0, y+aim*v);
        } else if (strcmp("down", cmd)==0) {
            aim+=v;
        } else if (strcmp("up", cmd) ==0) {
            aim-=v;
        }
    }
    printf("%ld\n", (long int)x*y);
    return 0;
}
