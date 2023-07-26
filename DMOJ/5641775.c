#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    // Assume answer is just one 2 and infinite ones?
    // But then a single 3 in the mix would add more than it takes away? NO!
    // But another 2 would!
    // So a combination of 1s and 2s
    // Which gives the largest combo?

    int n; scanf("%d", &n);
    int ones, twos;
    unsigned long long int best = 0ULL;
    unsigned long long int cur;
    for (int i=0; i<= n / 2; i++)
    {
        ones = n - 2*i;
        twos = i;
        cur = 1LL * ones*twos* (ones-1) / 2;
        if (cur > best) best = cur;
    }

    printf("%llu", best);

    return 0;
}