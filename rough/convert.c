#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>

typedef union {
    double d;
    uint64_t u;
} d_conv;

int main(void) {
    d_conv converter;

    converter.d = 2.71828;


    printf("%" PRIx64 "\n", converter.u);

    return 0;
}