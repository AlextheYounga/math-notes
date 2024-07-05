### Lesson 2.2: Limits and Continuity

#### Introduction to Limits

Welcome to the fascinating world of limits in calculus! In this lesson, we'll explore what limits are and how they're used to understand the behavior of functions as inputs approach a certain value. Think of a limit as trying to find out what value a function is heading towards as the input gets closer and closer to a specific point.

#### Understanding Limits with Python

Let's dive into the concept of limits with a hands-on Python example.

##### Example: Approaching a Point

Imagine you are walking towards a doorway, and with each step, you halve the distance to the door. You get closer and closer, but for a while, you don't actually reach the door—you just get very, very close. This idea mirrors what we explore in limits.

Here’s how we can simulate this in Python:

```python
import sympy as sp

# Define the variable and function
x = sp.symbols('x')
function = sp.sin(x) / x

# Point we are approaching
approaching_point = 0

# Calculate the limit
limit_value = sp.limit(function, x, approaching_point)
print(f"The limit of sin(x)/x as x approaches {approaching_point} is {limit_value}")
```

In this code, `sp.limit(function, x, approaching_point)` calculates what the function `sin(x)/x` heads towards as `x` gets closer to 0. Here, we don't actually plug 0 into the function, because it would be undefined. Instead, we're finding out the trend as we approach 0.

#### Visualizing Limits

Understanding limits isn't just about crunching numbers; it's about seeing them. Let's visualize our function and its limit as \( x \) approaches 0.

```python
import numpy as np
import matplotlib.pyplot as plt

# Create an array of x values around the approaching point
x_values = np.linspace(-10, 10, 400)
x_values = x_values[x_values != 0]  # Exclude zero to avoid division by zero error

# Evaluate function values
y_values = np.sin(x_values) / x_values

# Plotting the function
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='sin(x)/x')
plt.title('Graph of sin(x)/x')
plt.xlabel('x')
plt.ylabel('sin(x)/x')
plt.axhline(1, color='red', linestyle='--', label='Limit as x approaches 0')
plt.legend()
plt.show()
```

In the plot, the red dashed line at `y=1` shows the limit of the function as \( x \) approaches 0. You can see that no matter from which side \( x \) approaches zero, the value of `sin(x)/x` gets closer to 1.

#### Conceptual Understanding of Limits

Limits help us handle situations where direct evaluation would lead to undefined or ambiguous results. They are fundamental in calculus because they underpin the derivative and integral, which you'll learn about soon. Essentially, limits are about predicting trends and behaviors in mathematical functions, not unlike predicting the path of a planet or the growth of a population.

Remember, the beauty of limits lies in their ability to provide insights into the very small and the very large, capturing the essence of change and continuity in the mathematical universe. As we continue, we'll see just how powerful these concepts are in various fields of science and engineering!