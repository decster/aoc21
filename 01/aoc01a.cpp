#include <stdio.h>

int main(int argc, char **argv) {
    int cur, next;
    int ret = 0;
    scanf("%d", &cur);
    while (scanf("%d", &next) == 1) {
        if (next > cur) {
            ret++;
        }
        cur = next;
    }
    printf("%d\n", ret);
    return 0;
}
