#include <stdio.h>


int N, ans, x;
int main() {
    for (scanf("%d", &N); N--;) {
        scanf("%d", &x);
        ans ^= x;
    }
    printf("%d\n", ans);
    return 0;


}