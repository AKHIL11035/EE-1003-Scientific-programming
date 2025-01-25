import math
import matplotlib.pyplot as plt

# Function to calculate PMF using the binomial distribution
def calculate_pmf_binomial():
    n = 3  # Number of tosses
    p = 0.5  # Probability of heads
    pmf = [0] * (n + 1)  # List to hold PMF values for 0, 1, 2, 3 heads

    for k in range(n + 1):
        # Calculate binomial coefficient C(n, k) using iterative approach
        binomial_coefficient = 1
        for i in range(1, k + 1):
            binomial_coefficient *= (n - i + 1) / i

        # Compute PMF value for k heads
        pmf[k] = binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))
    
    return pmf

# Main execution
if __name__ == "__main__":
    # Calculate the PMF
    pmf_values = calculate_pmf_binomial()

    # Print the PMF values
    print("PMF values for 3 coin tosses:")
    for k in range(4):
        print(f"P({k} heads) = {pmf_values[k]:.4f}")

    # Plotting the PMF
    x = [0, 1, 2, 3]  # Number of heads (0 to 3)
    plt.stem(x, pmf_values, basefmt=" ", use_line_collection=True)
    plt.xlabel('Number of Heads')
    plt.ylabel('Probability')
  
    plt.xticks(x)  # Set x-axis labels to 0, 1, 2, 3
    plt.grid(True)
    plt.show()

