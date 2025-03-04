## Requirements
- Python 3.x
- NumPy (no need to include `requirements.txt` unless additional libraries are required)

## Compilation & Execution
To run the script, navigate to the project directory and execute the following command in the terminal:

**Command:**
Python `src/main/assignment_3.py`

## Methods Implemented
Euler’s Method is a first-order numerical procedure used to solve ordinary differential equations with a given initial value. The Runge-Kutta Method is a more advanced technique that provides better accuracy using a fourth-order approach.

## Problem Details
The differential equation to be solved is:

\( \frac{dy}{dt} = t - y^2 \)

The function is evaluated over the range \( 0 < t < 2 \), with an initial condition of \( f(0) = 1 \), and the numerical methods are applied with 10 iterations.

## Expected Output
The expected numerical results for the methods are:

- **Euler Method Result:** Computed value based on numerical approximation.
- **Runge-Kutta Method Result:** 1.2446380979332121
