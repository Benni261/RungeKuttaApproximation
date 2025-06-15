# Runge-Kutta Approximation
*Using Python to learn 4th Order Runge-Kutta Approximation accross a range of Ordinary Differential Equations*

## What is Runge-Kutta Approximation?
Runge-Kutta methods are a family of iterative methods for solving ordinary differential equations (ODEs). The 4th order Runge-Kutta method is particularly popular due to its balance between accuracy and computational efficiency. It approximates the solution of an ODE by evaluating the function at several points within each step, providing a more accurate estimate than simpler methods like Euler's method.

This promgram does not show different iterations with different step sizes like the euler method. Instead, it uses a fixed step size (which can be specified in the parameters) to approximate a solution of the ODEs.

## To Use the Program
1. Make a virtual environment and install the requirements.txt file.
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```
2. Run the main.py script.
```bash
python main.py
```
3. Follow the directions below.

## Adding Parameters


## The Equations
Here is an overview of the equations used in each script.

**Equation 1**
Differential Equation: $y'(x)=y$
Initial Condition: $y(0)=1$
Analytical Solution: $y(x)=e^x$

**Equation 2**
Differential Equation: $y'(x)=x+y$
Initial Condition: $y(0)=0$
Analytical Solution: $y(x)=e^x-x-1$

**Equation 3**
Differential Equation: $y'(x)=\cos(x)$
Initial Condition: $y(0)=0$
Analytical Solution: $y(x)=\sin(x)$