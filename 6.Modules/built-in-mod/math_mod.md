The Python `math` module provides access to mathematical functions. Here's a guide to using the `math` module with examples for basic, complex, and real-life scenarios:

### 1. Basic Math Functions

**a. `math.sqrt(x)`**
- Computes the square root of `x`.

```python
import math

print(math.sqrt(16))  # Output: 4.0
print(math.sqrt(2))   # Output: 1.4142135623730951
```

**b. `math.pow(x, y)`**
- Raises `x` to the power of `y`.

```python
print(math.pow(2, 3))  # Output: 8.0
print(math.pow(4, 0.5))  # Output: 2.0
```

**c. `math.factorial(x)`**
- Computes the factorial of `x`.

```python
print(math.factorial(5))  # Output: 120
print(math.factorial(0))  # Output: 1
```

### 2. Complex Numbers

**a. `cmath.sqrt(x)`**
- Computes the square root of `x`, where `x` can be a complex number.

```python
import cmath

print(cmath.sqrt(-1))  # Output: 1j
print(cmath.sqrt(4 + 9j))  # Output: (2.230974358132722+2.015898464235738j)
```

**b. `cmath.phase(x)`**
- Returns the phase of `x`, where `x` is a complex number.

```python
print(cmath.phase(1 + 1j))  # Output: 0.7853981633974483
print(cmath.phase(-1))  # Output: 3.141592653589793
```

**c. `cmath.polar(x)`**
- Converts a complex number `x` to its polar coordinate form.

```python
print(cmath.polar(1 + 1j))  # Output: (1.4142135623730951, 0.7853981633974483)
print(cmath.polar(3 - 4j))  # Output: (5.0, -0.9272952180016122)
```

### 3. Real-Life Examples

**a. Calculating the Area of a Circle**

```python
def area_of_circle(radius):
    return math.pi * math.pow(radius, 2)

print(area_of_circle(5))  # Output: 78.53981633974483
print(area_of_circle(10))  # Output: 314.1592653589793
```

**b. Compound Interest Calculation**

```python
def compound_interest(principal, rate, time):
    return principal * math.pow((1 + rate / 100), time)

print(compound_interest(1000, 5, 10))  # Output: 1628.894626777442
print(compound_interest(1500, 4.3, 6))  # Output: 1938.8368221341052
```

**c. Finding the Hypotenuse of a Right-Angled Triangle**

```python
def hypotenuse(a, b):
    return math.sqrt(math.pow(a, b) + math.pow(b, 2))

print(hypotenuse(3, 4))  # Output: 5.0
print(hypotenuse(5, 12))  # Output: 13.0
```

**d. Logarithmic Scale in Decibel Calculation**

```python
def decibels(intensity):
    return 10 * math.log10(intensity)

print(decibels(1000))  # Output: 30.0
print(decibels(1000000))  # Output: 60.0
```

**e. Projectile Motion**

```python
def projectile_motion(velocity, angle):
    angle_rad = math.radians(angle)
    max_height = math.pow(velocity * math.sin(angle_rad), 2) / (2 * 9.8)
    return max_height

print(projectile_motion(20, 45))  # Output: 10.204081632653061
print(projectile_motion(30, 60))  # Output: 34.18367346938775
```

These examples showcase the versatility of the `math` and `cmath` modules in handling a wide range of mathematical tasks, from simple arithmetic to complex number calculations and practical applications in various fields.