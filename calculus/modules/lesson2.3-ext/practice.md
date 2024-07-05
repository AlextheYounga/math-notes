Absolutely! Let's create a practice problem that will help you apply what you've learned about numerical differentiation and derivatives in Python.

### Practice Problem: Numerical Derivative of a Real-World Function

#### Problem Statement
You are given a function that models the height of a projectile (in meters) over time (in seconds):
```python
def height(time):
    return -4.9 * time**2 + 50 * time + 1.5  # Example function for height
```
This function represents the height of a projectile launched with an initial velocity and height. Your task is to:
1. Plot the height function over a range of time values.
2. Compute the numerical derivative of the height function, which represents the velocity of the projectile.
3. Plot the velocity function over the same range of time values.
4. Identify and print the time at which the projectile reaches its maximum height.

### Steps to Solve the Problem

1. **Plot the Height Function:**
    - Use `matplotlib` to plot the height function over a range of time values.
2. **Compute the Numerical Derivative:**
    - Create a function to approximate the derivative of the height function using a small value for \( h \).
3. **Plot the Velocity Function:**
    - Use `matplotlib` to plot the velocity function over the same range of time values.
4. **Find the Maximum Height:**
    - The maximum height corresponds to the point where the velocity is zero. Use the velocity function to find and print this time.

Here’s a template to get you started:

```python
import matplotlib.pyplot as plt
import numpy as np

# Define the height function
def height(time):
    return -4.9 * time**2 + 50 * time + 1.5

# Define the numerical derivative function
def numerical_derivative(func, time, h=1e-5):
    return (func(time + h) - func(time - h)) / (2 * h)

# Define the velocity function as the derivative of the height function
def velocity(time):
    return numerical_derivative(height, time)

# Generate time values
time_values = np.linspace(0, 12, 400)  # Adjust the range as necessary
height_values = height(time_values)
velocity_values = velocity(time_values)

# Plot the height function
plt.plot(time_values, height_values, label='Height (time)')
plt.xlabel('Time (seconds)')
plt.ylabel('Height (meters)')
plt.title('Height of Projectile over Time')
plt.legend()
plt.grid(True)
plt.show()

# Plot the velocity function
plt.plot(time_values, velocity_values, label='Velocity (time)', color='red')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (meters/second)')
plt.title('Velocity of Projectile over Time')
plt.legend()
plt.grid(True)
plt.show()

# Find the time at which the projectile reaches its maximum height
max_height_time = time_values[np.argmax(height_values)]
print(f"The projectile reaches its maximum height at approximately t = {max_height_time:.2f} seconds")
```

### Instructions
1. **Run the provided code template.**
2. **Analyze the plots to understand the behavior of the height and velocity functions.**
3. **Observe the time at which the height is maximum and verify it using the velocity function plot.**

This exercise will help reinforce your understanding of numerical derivatives and how they apply to real-world functions. If you have any questions or need further guidance, feel free to ask!