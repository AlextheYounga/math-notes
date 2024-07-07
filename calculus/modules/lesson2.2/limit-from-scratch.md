### Lesson 2.2 Follow-Up: Calculating Limits in Python from Scratch

#### Introduction

In this follow-up lesson, we'll delve into how Python can be used to calculate limits, specifically attempting to recreate a simple version of SymPy's limit function from scratch. We'll explore the numerical approach to understanding limits, which provides a practical grounding in how limits might be computed in a computational environment.

#### Concept of Limits - Numerical Approach

When calculating limits numerically, we approximate the value a function approaches as its argument gets close to a certain point. This method doesn't always give exact answers like algebraic methods do, but it can provide a good approximation in many cases, especially when dealing with functions that are complex or not easily simplified.

#### Building a Basic Limit Function

We'll build a basic Python function that estimates the limit of another function as \( x \) approaches a particular value from the left or the right. We'll use a simple approach where we incrementally move closer to the target point and observe the function's value.

Here's how we can structure our custom limit function:

1. **Define the Target Function**: This will be the mathematical function whose limit we want to compute.
2. **Approach Point**: This is the point \( x \) that we are approaching in our limit calculation.
3. **Direction**: Specify whether the limit is approached from the left (negative direction) or the right (positive direction).
4. **Step Size Reduction**: Gradually reduce the step size as we get closer to the approach point to refine our approximation.

#### Python Implementation

Here's a Python script that implements these ideas:

```python
import numpy as np

def custom_limit(func, approach_point, direction="right", precision=1e-7):
    """
    Estimate the limit of a function as x approaches a certain point from left or right.

    Args:
    func (callable): The function for which the limit is calculated.
    approach_point (float): The point which x approaches.
    direction (str): 'left' or 'right' approach.
    precision (float): The precision of the approach.

    Returns:
    float: The estimated limit of the function.
    """
    step_size = 0.1  # initial step size
    if direction == "left":
        step_size = -step_size
    
    x = approach_point + step_size
    previous_value = func(x)
    
    while abs(x - approach_point) > precision:
        step_size *= 0.5
        x += step_size
        current_value = func(x)
        
        # If values start oscillating or diverging, break out of the loop
        if abs(current_value - previous_value) > abs(previous_value):
            return float('nan')  # Return NaN to indicate no limit
        
        previous_value = current_value
        
    return current_value

# Example function
def f(x):
    return (x**2 - 4) / (x - 2)

# Estimate limit
limit_estimation = custom_limit(f, 2, "right")
print("Estimated limit from the right:", limit_estimation)
```

#### Explanation

- **Function Definition**: We define a custom function `custom_limit` that takes a function `func`, an `approach_point`, a `direction`, and a `precision`.
- **Initial Setup**: We start with an initial step size and adjust it based on the direction of approach.
- **Loop for Refinement**: We gradually reduce the step size and update our \( x \) value until the change in \( x \) is below the precision threshold.
- **Value Stability Check**: We check if the function value starts oscillating or diverging, in which case we return `NaN` to indicate the limit does not exist or cannot be determined.

#### Conclusion

This basic limit calculator provides a framework for understanding how numerical approaches can be used to estimate limits. While this method is useful for understanding and teaching, it lacks the robustness and depth of methods used in libraries like SymPy, which can handle a wider range of functions and more complex mathematical scenarios. This exercise serves as a great starting point for exploring numerical computation and the practical challenges of calculating limits.