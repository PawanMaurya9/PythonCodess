# Write a Python program that prints the Fibonacci series up to n terms.
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Get the number of terms from the user
n_terms = int(input("Enter the number of terms: "))

# Print the Fibonacci series
print(f"Fibonacci series up to {n_terms} terms:")
fibonacci_series(n_terms)