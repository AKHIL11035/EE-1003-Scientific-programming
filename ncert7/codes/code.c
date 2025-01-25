#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to calculate PMF using the binomial distribution
void calculate_pmf_binomial(double *pmf) {
    int n = 3; // Number of tosses
    double p = 0.5; // Probability of heads
    for (int k = 0; k <= n; k++) {
        // Calculate binomial coefficient C(n, k) using iterative approach
        double binomial_coefficient = 1;
        for (int i = 1; i <= k; i++) {
            binomial_coefficient *= (double)(n - i + 1) / i;
        }

        // Compute PMF value for k heads
        pmf[k] = binomial_coefficient * pow(p, k) * pow(1 - p, n - k);
    }
}

// Main function
int main() {
    double pmf[4]; // Array to hold PMF values for 0, 1, 2, 3 heads
    calculate_pmf_binomial(pmf);

    // Print the PMF values
    printf("PMF values for 3 coin tosses:\n");
    for (int k = 0; k <= 3; k++) {
        printf("P(%d heads) = %.4f\n", k, pmf[k]);
    }

    return 0;
}

