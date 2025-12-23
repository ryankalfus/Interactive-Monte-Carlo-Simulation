# -*- coding: utf-8 -*-
"""Pi_Simulation.ipynb"""

import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets
from IPython.display import display

def plot_monte_carlo(num_dots_str):
    try:
        num_dots = int(num_dots_str)
        if num_dots < 1:
            num_dots = 1 # Ensure minimum is 1
        elif num_dots > 100000:
            num_dots = 100000 # Ensure maximum is 100,000
    except ValueError:
        num_dots = 100 # Default to 100 if not a valid number

    # --- First plot: Monte Carlo Simulation ---
    plt.figure(figsize=(7, 7))
    ax_sim = plt.gca()

    # Draw the square (from -1 to 1 on both x and y axes)
    square_x = [-1, 1, 1, -1, -1]
    square_y = [-1, -1, 1, 1, -1]
    ax_sim.plot(square_x, square_y, 'k-', linewidth=2, label='Square')

    # Generate random dots
    x_dots = np.random.uniform(-1, 1, num_dots)
    y_dots = np.random.uniform(-1, 1, num_dots)

    # Plot dots (moved before circle to be underneath)
    ax_sim.scatter(x_dots, y_dots, color='red', s=5, alpha=0.6, label='Random Dots')

    # Draw the inscribed circle (radius 1, center 0,0)
    circle = plt.Circle((0, 0), 1, color='blue', fill=False, linewidth=2, label='Inscribed Circle')
    ax_sim.add_artist(circle)

    # Calculate dots inside the circle
    distances = np.sqrt(x_dots**2 + y_dots**2)
    dots_in_circle = np.sum(distances <= 1)

    # Calculate Pi approximation
    pi_approx = 4 * dots_in_circle / num_dots


    ax_sim.set_xlim([-1.5, 1.5])
    ax_sim.set_ylim([-1.5, 1.5])
    ax_sim.set_aspect('equal', adjustable='box')
    ax_sim.set_title(f'Monte Carlo Pi Approximation with {num_dots} Dots')
    ax_sim.set_xlabel('X-axis')
    ax_sim.set_ylabel('Y-axis')
    ax_sim.legend()
    plt.grid(True)
    plt.show()

    # --- Second plot: Pi Approximation Details ---
    plt.figure(figsize=(7, 2)) # Smaller figure for text
    ax_text = plt.gca()
    ax_text.set_xlim(0, 1)
    ax_text.set_ylim(0, 1)
    ax_text.axis('off') # Hide axes

    # Add text information to the plot
    ax_text.text(0.1, 0.8, f'Dots in circle (x): {dots_in_circle}', fontsize=12, ha='left', va='center')
    ax_text.text(0.1, 0.5, f'Total dots (y): {num_dots}', fontsize=12, ha='left', va='center')
    ax_text.text(0.1, 0.2, f'Pi approximation: {pi_approx:.4f}', fontsize=14, ha='left', va='center', fontweight='bold')
    plt.show()

    # --- Third plot: Equation Explanation ---
    plt.figure(figsize=(7, 3)) # Figure for equation explanation
    ax_eq = plt.gca()
    ax_eq.set_xlim(0, 1)
    ax_eq.set_ylim(0, 1)
    ax_eq.axis('off') # Hide axes

    ax_eq.text(0.5, 0.8, r'Monte Carlo Pi Approximation:', fontsize=14, ha='center', va='center', fontweight='bold')
    ax_eq.text(0.5, 0.5, r'$\frac{\text{Area of Circle}}{\text{Area of Square}} = \frac{\text{Pi} r^2}{(2r)^2} = \frac{\text{Pi}}{4}$', fontsize=16, ha='center', va='center')
    ax_eq.text(0.5, 0.2, r'$\text{Pi} \approx 4 \times \frac{\text{Number of dots in circle}}{\text{Total number of dots}}$', fontsize=16, ha='center', va='center')

    plt.show()

# Create a text input widget for the number of dots
num_dots_input = widgets.Text(
    value='100',
    description='Number of Dots:',
    disabled=False
)

# Use interactive to link the text input to the plotting function
interactive_plot = widgets.interactive(plot_monte_carlo, num_dots_str=num_dots_input)

# Display the interactive plot
display(interactive_plot)
