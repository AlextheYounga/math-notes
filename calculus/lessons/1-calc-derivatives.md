# Part 1

Great! Welcome to your first lesson in calculus through Python programming. We'll start with the fundamental concept of calculus: the **derivative**. Understanding derivatives is crucial because they represent how things change. This concept is everywhere in the real world, from physics to economics to biology.

### Introduction to Derivatives

#### What is a Derivative?

A derivative measures how a function changes as its input changes. For instance, if you have a function that describes the position of a car over time, the derivative of this function will tell you the car's speed at any given moment.

To grasp this concept, let's look at it from a Python programming perspective.

### Python Example: Numerical Derivative

First, we'll write a Python function to compute the derivative numerically. This method is based on the definition of the derivative:

```math
\[ f'(x) = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x} \]
```


Here's a simple Python function to approximate the derivative:

```python
import matplotlib.pyplot as plt
import numpy as np

def numerical_derivative(function, x, delta_x=1e-5):
    """
    Compute the numerical derivative of a function at a given point.

    :param function: The function for which to compute the derivative
    :param x: The point at which to compute the derivative
    :param delta_x: A small change in x to compute the difference quotient
    :return: The numerical derivative of the function at point x
    """
    return (function(x + delta_x) - function(x)) / delta_x

# Example usage
def example_function(x):
    return x**2

# Calculate the derivative at x = 3
x_point = 3
derivative_at_x = numerical_derivative(example_function, x_point)
print(f"The numerical derivative of x^2 at x = {x_point} is approximately {derivative_at_x}")
```

### Explanation

1. **Function Definition**: `numerical_derivative` takes three arguments:
   - `function`: The function we want to differentiate.
   - `x`: The point at which we want to find the derivative.
   - `delta_x`: A small number to compute the difference quotient (default is \(10^{-5}\)).

2. **Difference Quotient**: Inside the function, we compute the difference quotient, which is \(\frac{f(x + \Delta x) - f(x)}{\Delta x}\).

3. **Example Function**: We define `example_function` as \( f(x) = x^2 \). We know from calculus that the derivative of \( x^2 \) is \( 2x \), so at \( x = 3 \), the derivative should be \( 6 \).

4. **Result**: We compute the derivative at \( x = 3 \) using our numerical method and print the result.

### Visualization

Let's visualize this to get a better understanding. We'll plot the function \( f(x) = x^2 \) and its derivative \( f'(x) = 2x \).

```python
# Define the derivative function
def exact_derivative(x):
    return 2 * x

# Generate x values
x_values = np.linspace(-10, 10, 400)
# Compute y values for the function and its derivative
y_values = example_function(x_values)
dy_values = exact_derivative(x_values)

# Plot the function and its derivative
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x) = x^2')
plt.plot(x_values, dy_values, label="f'(x) = 2x", linestyle='--')
plt.scatter([x_point], [example_function(x_point)], color='red')  # Point of interest
plt.scatter([x_point], [derivative_at_x], color='green')  # Numerical derivative
plt.legend()
plt.title('Function and its Derivative')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
```

### Explanation of the Plot

- **Blue Line**: The function \( f(x) = x^2 \).
- **Orange Line**: The exact derivative \( f'(x) = 2x \).
- **Red Point**: The value of \( f(3) = 9 \).
- **Green Point**: The numerical derivative at \( x = 3 \).

This visualization helps you see how the function and its derivative relate to each other. The slope of the function at any point \( x \) is given by the derivative at that point.

### Key Takeaways

1. **Derivative Concept**: It measures the rate of change of a function.
2. **Numerical Derivative**: We can approximate derivatives using the difference quotient.
3. **Visualization**: Plotting functions and their derivatives helps in understanding the relationship between them.

Do you have any questions about this introduction to derivatives, or is there any part you'd like to dive deeper into? If everything is clear, just let me know with "Understood. Next lesson."