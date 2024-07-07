### Practice Python Question for Lesson 2.2

#### Question: Analyzing and Visualizing Continuity

You are given the function \( f(x) = \frac{x^2 - 4}{x - 2} \). This function appears to have an issue at \( x = 2 \). Your task is to analyze and visualize the function to understand its behavior around \( x = 2 \), and determine if the function is continuous at this point or not.

#### Steps:

1. **Analyze the Function**: Simplify the function algebraically, if possible, and discuss what you observe about the form of the function when \( x = 2 \).
   
2. **Calculate Limits**: Using Python, calculate the left-hand and right-hand limits of \( f(x) \) as \( x \) approaches 2. Use this information to determine if there's a limit at \( x = 2 \) and if it matches the function value at \( x = 2 \) (if defined).

3. **Visualize the Function**: Plot the function over the range \( x = 0 \) to \( x = 4 \). Ensure you handle any issues at \( x = 2 \) in your plot, such as removing discontinuities for clearer visualization.

4. **Conclusion**: Based on your calculations and the plot, state whether the function is continuous at \( x = 2 \) and explain why.

#### Python Skeleton Code

```python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the variable and function
x = sp.symbols('x')
numerator = x**2 - 4
denominator = x - 2
function = numerator / denominator

# Simplify the function if possible
simplified_function = sp.simplify(function)

# Display the simplified function
print(f"Simplified function: {simplified_function}")

# Calculate the limits
left_limit = sp.limit(function, x, 2, dir='-')
right_limit = sp.limit(function, x, 2, dir='+')

# Print the calculated limits
print(f"Left-hand limit as x approaches 2: {left_limit}")
print(f"Right-hand limit as x approaches 2: {right_limit}")

# Define the range for x values excluding the discontinuity at x = 2
x_values = np.linspace(0, 4, 400)
x_values = x_values[x_values != 2]

# Evaluate the simplified function values
y_values = [simplified_function.subs(x, val) for val in x_values]

# Plotting the function
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=f'Plot of {simplified_function}')
plt.title('Graph of the function over x = 0 to x = 4')
plt.xlabel('x')
plt.ylabel(f'{simplified_function}')
plt.axvline(2, color='red', linestyle='--', label='x = 2')
plt.legend()
plt.show()

# Conclusion based on the calculations and plot
```

This exercise will help you understand how to handle and visualize functions that might appear to have discontinuities, using Python's powerful symbolic and numerical computation capabilities.