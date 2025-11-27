#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>

// Define a union as described in Lab 2 Section 2.3.1 [cite: 246]
// This allows the double and uint64_t to share the same memory location.
typedef union {
    double d;
    uint64_t u;
} d_conv;

int main(void) {
    d_conv converter;

    // Assign the specific double value required by Q2d 
    converter.d = 2.71828;

    // Print the bitwise representation in hex using the C99 PRIx64 format specifier
    // The manual notes that writing to one member changes the value of both [cite: 251]
    printf("%" PRIx64 "\n", converter.u);

    return 0;
}