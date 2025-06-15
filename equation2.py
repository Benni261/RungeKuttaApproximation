# Euler's Method for the differential equation y'(x) = y with initial condition y(0) = 1
import math
import matplotlib.pyplot as plt

def f(x, y):
    """The function representing the differential equation y'(x) = y."""
    return x+y

def f_analytical(x):
    """The analytical solution of the differential equation y'(x) = y."""
    return math.exp(x)-x-1

def execute(step_size=1, x_stoppper=10.0):
    """Run the Euler method for the given step size and x stopper."""
    x = 0.0
    y = 0.0

    # Initialize lists to store x and y values for plotting
    x_values = []
    y_values = []
    x_analytical_values = [x/100 for x in range(0, int(x_stoppper*100)+1)]
    y_analytical_values = [f_analytical(x) for x in x_analytical_values]

    while x < x_stoppper:
        slope_k1 = f(x,y)
        # print(f"X Coords: {x}, Y Coords: {y}")
        # print(f"Slope K1: {slope_k1}")
        slope_k2 = f(x+(step_size/2),y+(slope_k1*step_size/2))
        # print(f"Slope K2: {slope_k2}")
        slope_k3 = f(x+(step_size/2),y+(slope_k2*step_size/2))
        # print(f"Slope K3: {slope_k3}")
        slope_k4 = f(x+step_size,y+(slope_k3*step_size))
        # print(f"Slope K4: {slope_k4}")
        slope = (step_size/6)*(slope_k1+(2*slope_k2)+(2*slope_k3)+slope_k4)
        # print(f"Slope: {slope}\n")
        x += step_size
        y += slope

        # Store the values for plotting
        x_values.append(x)
        y_values.append(y)

    print(f"Step Size: {step_size}")
    print(f"Analytical: {f_analytical(x_stoppper)}")
    print(f"Euler Approximation: {y}")
    print(f"Difference: {f_analytical(x_stoppper) - y}\n")
    
    # print(x_values, "\n")
    # print(y_values, "\n")
    # print(y_analytical_values, "\n")

    # Plotting the results

    plt.figure(figsize=(10, 6))
    plt.plot(x_analytical_values, y_analytical_values, label='Analytical Solution ($e^x$)', color='red', linestyle='-')
    plt.plot(x_values, y_values, label=f'Runge-Kutta Approximation', color='blue', linestyle='--')
    plt.title('Runge-Kutta (Order of 4) vs. Analytical Solution for y\'(x) = y')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    execute()