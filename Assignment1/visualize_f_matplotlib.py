import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import mpld3
from mpld3 import plugins

def save_figure_to_html(fig, filename):
    """Save the matplotlib figure to an interactive HTML file using mpld3."""
    mpld3.save_html(fig, filename)
    plt.close(fig)  # Close the figure after saving

def visualize_trajectory(trajectory, floor_plan_filename, width_meter, height_meter, title=None, show=False):
    # Sort trajectory by first column (assumed to be time or sequence order)
    trajectory = trajectory[np.argsort(trajectory[:, 0])]
    
    # Load the background image (floor plan)
    img = mpimg.imread(floor_plan_filename)

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(10, 10 * height_meter / width_meter))

    # Show the background image
    ax.imshow(img, extent=[0, width_meter, 0, height_meter])

    # Prepare trajectory sizes and colors for the plot
    size_list = [6] * trajectory.shape[0]
    size_list[0] = 10  # Start point size
    size_list[-1] = 10  # End point size

    color_list = ['blue'] * trajectory.shape[0]
    color_list[0] = 'green'  # Start point color
    color_list[-1] = 'red'  # End point color

    # **Add this to plot the line connecting the points**
    ax.plot(trajectory[:, 0], trajectory[:, 1], color='blue', linestyle='-', linewidth=2, label='Path')

    # Plot the trajectory on top of the background
    scatter = ax.scatter(trajectory[:, 0], trajectory[:, 1], s=size_list, c=color_list, label='Trajectory Points')
    # Add start and end point labels
    ax.text(trajectory[0, 0], trajectory[0, 1], 'Start', color='green', fontsize=12)
    ax.text(trajectory[-1, 0], trajectory[-1, 1], 'End', color='red', fontsize=12)

    # Set axis limits to match the floor plan
    ax.set_xlim(0, width_meter)
    ax.set_ylim(0, height_meter)

    # Set axis labels and title
    ax.set_xlabel('X Coordinate (meters)')
    ax.set_ylabel('Y Coordinate (meters)')
    if title:
        ax.set_title(title)

    # Add hover functionality using mpld3
    labels = [f"Point {i}: ({x:.2f}, {y:.2f})" for i, (x, y) in enumerate(trajectory)]
    tooltip = plugins.PointLabelTooltip(scatter, labels=labels)
    plugins.connect(fig, tooltip)

    # Show the plot or save it as needed
    if show:
        mpld3.display(fig)

    return fig

def visualize_trajectory_step_position(trajectory, floor_plan_filename, width_meter, height_meter, title=None, mode='o', show=False):
    # Sort trajectory by first column (assumed to be time or sequence order)
    trajectory = trajectory[np.argsort(trajectory[:, 0])]

    # Load the background image (floor plan)
    img = mpimg.imread(floor_plan_filename)

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(10, 10 * height_meter / width_meter))

    # Show the background image
    ax.imshow(img, extent=[0, width_meter, 0, height_meter])

    # Prepare trajectory sizes and colors for the plot
    size_list = [6] * trajectory.shape[0]
    size_list[0] = 10  # Start point size
    size_list[-1] = 10  # End point size

    color_list = ['blue'] * trajectory.shape[0]
    color_list[0] = 'green'  # Start point color
    color_list[-1] = 'red'  # End point color

    # Plot the trajectory on top of the background
    #ax.plot(trajectory[:, 0], trajectory[:, 1], 'bo-', markersize=5, label='Trajectory')
    #ax.plot(trajectory[:, 0], trajectory[:, 1], color='blue', label='Trajectory')  # Lines between points
    scatter = ax.scatter(trajectory[:, 0], trajectory[:, 1], s=size_list, edgecolors=color_list, marker=mode, facecolors='none', linewidth=0.5)

    # # Add start and end point labels
    # ax.text(trajectory[0, 0], trajectory[0, 1], 'Start', color='green', fontsize=12)
    # ax.text(trajectory[-1, 0], trajectory[-1, 1], 'End', color='red', fontsize=12)

    # Set axis limits to match the floor plan
    ax.set_xlim(0, width_meter)
    ax.set_ylim(0, height_meter)

    # Set axis labels and title
    ax.set_xlabel('X Coordinate (meters)')
    ax.set_ylabel('Y Coordinate (meters)')
    if title:
        ax.set_title(title)

    # Add hover functionality using mpld3
    labels = [f"Point {i}: ({x:.2f}, {y:.2f})" for i, (x, y) in enumerate(trajectory)]
    tooltip = plugins.PointLabelTooltip(scatter, labels=labels)
    plugins.connect(fig, tooltip)


    # Show the plot or save it as needed
    if show:
        mpld3.display(fig)

    return fig

def visualize_heatmap(position, value, floor_plan_filename, width_meter, height_meter, colorbar_title="colorbar", title=None, show=False):
    # Load the background image (floor plan)
    img = mpimg.imread(floor_plan_filename)

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(10, 10 * height_meter / width_meter))

    # Show the background image
    ax.imshow(img, extent=[0, width_meter, 0, height_meter])

    # Create a scatter plot over the floor plan
    scatter = ax.scatter(position[:, 0], position[:, 1], c=value, cmap='rainbow', s=7)

    # Add hover functionality using mpld3
    labels = [f"Position: ({x:.2f}, {y:.2f}), Value: {v:.2f}" for x, y, v in zip(position[:, 0], position[:, 1], value)]
    tooltip = plugins.PointLabelTooltip(scatter, labels=labels)
    plugins.connect(fig, tooltip)

    # Add a colorbar
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label(colorbar_title)

    # Set axis limits to match the floor plan
    ax.set_xlim(0, width_meter)
    ax.set_ylim(0, height_meter)

    # Set axis labels and title
    ax.set_xlabel('X Coordinate (meters)')
    ax.set_ylabel('Y Coordinate (meters)')
    if title:
        ax.set_title(title)

    # Show the plot or save it as needed
    if show:
        mpld3.display(fig)

    return fig
