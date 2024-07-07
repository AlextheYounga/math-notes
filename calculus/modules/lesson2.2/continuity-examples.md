### Lesson 2.2: Exploring Continuity Through Examples

#### Introduction to Continuity

In this section, we'll explore the concept of continuity—a fundamental idea in calculus that deals with smooth transitions within functions. A function is continuous at a point if there are no breaks, jumps, or gaps in its graph at that point. More practically, you can think of continuity as the property that allows you to draw the graph of the function without lifting your pen off the paper.

#### Python Example: Checking Continuity

Let’s examine continuity through some examples using Python. We’ll start by defining a simple function and then check if it's continuous at certain points.

##### Example: Continuous Function

Consider the function \( f(x) = x^2 \). It's a basic quadratic function, and we expect it to be continuous everywhere. Let’s confirm this using Python, focusing on a few points.

```python
import sympy as sp

# Define the variable and function
x = sp.symbols('x')
function = x**2

# Points to check continuity
points_to_check = [-1, 0, 1, 2]

# Check continuity at each point
continuity_results = {}
for point in points_to_check:
    left_limit = sp.limit(function, x, point, dir='-')
    right_limit = sp.limit(function, x, point, dir='+')
    function_value = function.subs(x, point)
    # Check if left limit, right limit, and function value are the same
    is_continuous = (left_limit == right_limit == function_value)
    continuity_results[point] = is_continuous

# Print results
for point, is_cont in continuity_results.items():
    print(f"The function is {'continuous' if is_cont else 'not continuous'} at x = {point}")
```

In this code, we use Sympy to calculate the left and right limits at each point and compare them with the function's value at that point. For \( f(x) = x^2 \), the limits and function values should be identical at all checked points, confirming its continuity.

#### Example: Discontinuous Function

Now, let's consider a function that isn’t continuous everywhere. A common example is \( f(x) = \frac{1}{x} \).

```python
# Redefine the function for 1/x
function = 1/x

# Points to check continuity (excluding zero initially)
points_to_check = [-1, 1, 2]

# Checking continuity again with the same loop
for point in points_to_check:
    left_limit = sp.limit(function, x, point, dir='-')
    right_limit = sp.limit(function, x, point, dir='+')
    function_value = function.subs(x, point)
    is_continuous = (left_limit == right_limit == function_value)
    print(f"The function is {'continuous' if is_continuous else 'not continuous'} at x = {point}")
```

This function is continuous at all points except at \( x = 0 \) where it is undefined (division by zero). The function has a vertical asymptote at \( x = 0 \), representing a discontinuity.

#### Visualizing Discontinuity

Let’s visualize the discontinuity at \( x = 0 \) for \( \frac{1}{x} \).

```python
import numpy as np
import matplotlib.pyplot as plt

# Define x values around 0 but not including 0
x_values = np.linspace(-2, 2, 400)
x_values = x_values[x_values != 0]  # Exclude zero

# Evaluate function values
y_values = 1 / x_values

# Plotting the function
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='1/x')
plt.title('Graph of 1/x')
plt.xlabel('x')
plt.ylabel('1/x')
plt.axvline(0, color='red', linestyle='--', label='Discontinuity at x = 0')
plt.ylim(-10, 10)  # Limit y-axis to avoid extreme values near zero
plt.legend()
plt.show()
```

In this plot, the red dashed line indicates the point of discontinuity at \( x = 0 \), where the function "jumps" from negative infinity to positive infinity.

#### Conceptual Takeaway

Continuity is essential in calculus because it ensures the predictable behavior of functions within their domains. Discontinuities, where they occur, often require special attention in calculus as they can affect limits, derivatives, and integrals. Understanding and identifying continuity helps in grasping more complex calculus concepts that build on this foundation.