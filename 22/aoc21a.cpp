#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;


struct Cmd {
    Cmd(){}
    bool on;
    long rs[6];
};

int main(int argc, char** argv) {
    vector<Cmd> cmds;
    char cmd[8];
    int rx[2], ry[2], rz[2];
    map<int, int> xs, ys, zs;
    while (7 == scanf("%s x=%d..%d,y=%d..%d,z=%d..%d", cmd, rx, rx+1, ry, ry+1, rz, rz+1)) {
        cmds.emplace_back();
        Cmd& c = cmds.back();
        c.on = cmd[1] == 'n';
        c.rs[0] = rx[0];
        c.rs[1] = rx[1];
        c.rs[2] = ry[0];
        c.rs[3] = ry[1];
        c.rs[4] = rz[0];
        c.rs[5] = rz[1];
        xs[rx[0]] = 0;
        xs[rx[1]+1] = 0;
        ys[ry[0]] = 0;
        ys[ry[1]+1] = 0;
        zs[rz[0]] = 0;
        zs[rz[1]+1] = 0;
    }
    int X = xs.size();
    int Y = ys.size();
    int Z = zs.size();
    printf("X:%d, Y:%d Z:%d\n", X, Y, Z);
    vector<long> vx;
    for (auto& e: xs) {
        e.second = vx.size();
        vx.push_back(e.first);
        printf("%d,", e.first);
    }
    printf("\n");
    vector<long> vy;
    for (auto& e: ys) {
        e.second = vy.size();
        vy.push_back(e.first);
        printf("%d,", e.first);
    }
    printf("\n");
    vector<long> vz;
    for (auto& e: zs) {
        e.second = vz.size();
        vz.push_back(e.first);
        printf("%d,", e.first);
    }
    printf("\n");
    vector<int> grid(X*Y*Z, 0);
    for (Cmd& c : cmds) {
        int gxs = xs.lower_bound(c.rs[0])->second;
        int gxe = xs.lower_bound(c.rs[1]+1)->second;
        int gys = ys.lower_bound(c.rs[2])->second;
        int gye = ys.lower_bound(c.rs[3]+1)->second;
        int gzs = zs.lower_bound(c.rs[4])->second;
        int gze = zs.lower_bound(c.rs[5]+1)->second;
        printf("set grid %d..%d,%d..%d,%d..%d\n", gxs, gxe, gys, gye, gzs, gze);
        for (int i=gxs;i<gxe;i++) {
            for (int j=gys;j<gye;j++) {
                for (int k=gzs;k<gze;k++) {
                    grid[i*Y*Z + j*Z + k] = c.on;
                }
            }
        }
    }
    long ret = 0;
    for (int i=0;i<vx.size()-1;i++) {
        for (int j=0;j<vy.size()-1;j++) {
            for (int k=0;k<vz.size()-1;k++) {
                if (grid[i*Y*Z + j*Z + k]) {
                    ret += (vx[i+1] - vx[i]) * (vy[j+1] - vy[j]) * (vz[k+1] - vz[k]);
                }
            }
        }
    }
    printf("%ld\n", ret);
    return 0;
}
