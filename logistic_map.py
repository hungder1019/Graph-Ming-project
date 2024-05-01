import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x, scale):
    # Logistic growth model adapted to scale for the specific application
    return r * x * (1 - x) * scale  # Scale to ng/L for methylmercury concentration

def plot_cobweb(r, num_iterations, initial_value, max_mines, max_mercury, pause_time):
    x = np.linspace(0, 1, 400)
    y = logistic_map(r, x, max_mercury)
    
    # Setting up the figure and axis
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.plot(x * max_mines, y, 'k', lw=2, label='Logistic map: Methylmercury concentration')  # Scale x-axis to represent number of mines
    ax.plot(x * max_mines, x * max_mercury, 'b', lw=1, label='y = x (scaled)')  # Line y = x scaled for methylmercury
    
    # Cobwebbing with scaling
    x_n = initial_value
    for i in range(num_iterations):
        y_n = logistic_map(r, x_n, max_mercury)
        ax.plot([x_n * max_mines, x_n * max_mines], [x_n * max_mercury, y_n], 'r', lw=1)  # Vertical line, scaled
        ax.plot([x_n * max_mines, y_n * max_mines / max_mercury], [y_n, y_n], 'r', lw=1)  # Horizontal line, scaled
        if not plt.fignum_exists(fig.number):
            print("Plot window closed by user.")
            break
        plt.pause(pause_time)
        if not plt.fignum_exists(fig.number): #Put in twice in order to make sure user doesn't have to wait for pause time
            print("Plot window closed by user.")
            break
        x_n = y_n / max_mercury  # Update the current point, scale back for next iteration

    # Set up plot limits and labels
    ax.set_xlim(0, max_mines)  # Range of mines
    ax.set_ylim(0, max_mercury)  # Range of methylmercury in ng/L
    ax.set_title(f'Cobweb Plot for r = {r} with Mines and Methylmercury')
    ax.set_xlabel('Number of Mines')
    ax.set_ylabel('Methylmercury Concentration (ng/L)')
    ax.legend()
    plt.show()

# User input for parameters
print("Note: If you have a pause time greater than 0 seconds, then wait until the end to fully analyze the meaning of each line and understand the plot information displayed.\nThis will be where axes are labeled.")
print("Warning: Entering certain values might result in a plot where no iterations are visible, depending on the dynamics of the logistic map at those settings.")
r_value = float(input("Enter the value of r (best to choose values between 0 and 4): "))
max_mines = float(input("Enter the maximum number of mines present (e.g., 80): "))
max_mercury = float(input("Enter the maximum methylmercury concentration in ng/L (e.g., 60): "))
initial_value = 0.2
num_iterations = float(input("Enter the amount of iterations you would want (a decimal value will truncate): "))
num_iterations = int(num_iterations)
pause_time = float(input("Enter the pause time in seconds between iterations (Enter 0 if you just want the diagram; best to choose 0.2 to 0.5 if pause_time is desired): "))

plot_cobweb(r_value, num_iterations, initial_value, max_mines, max_mercury, pause_time)
