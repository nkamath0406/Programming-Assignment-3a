import numpy as np

def euler_method(f, t0, y0, t_end, n):
    h = (t_end - t0) / n
    t_values = np.linspace(t0, t_end, n + 1)
    y_values = np.zeros(n + 1)
    y_values[0] = y0
    
    for i in range(n):
        y_values[i + 1] = y_values[i] + h * f(t_values[i], y_values[i])
    
    return y_values[-1]

def runge_kutta_method(f, t0, y0, t_end, n):
    h = (t_end - t0) / n
    t_values = np.linspace(t0, t_end, n + 1)
    y_values = np.zeros(n + 1)
    y_values[0] = y0
    
    for i in range(n):
        k1 = h * f(t_values[i], y_values[i])
        k2 = h * f(t_values[i] + h / 2, y_values[i] + k1 / 2)
        k3 = h * f(t_values[i] + h / 2, y_values[i] + k2 / 2)
        k4 = h * f(t_values[i] + h, y_values[i] + k3)
        
        y_values[i + 1] = y_values[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    
    return y_values[-1]

def function(t, y):
    return t - y ** 2

if __name__ == "__main__":
    euler_result = euler_method(function, 0, 1, 2, 10)
    runge_kutta_result = runge_kutta_method(function, 0, 1, 2, 10)
    print(f"Euler Method Result: {euler_result}")
    print(f"Runge-Kutta Method Result: {runge_kutta_result}")
