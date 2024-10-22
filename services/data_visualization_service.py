from matplotlib import pyplot as plt
import airfrans as af

def visualize_simulation(simulation: af.Simulation) -> None:
    """Visualize various simulation attributes using scatter plots.

    Args:
        simulation (af.Simulation): The simulation object containing data.
    """
    _, ax = plt.subplots(2, 3, figsize=(36, 12))

    # Plot position vs. velocity, pressure, sdf, nu_t, and airfoil attributes
    ax[0, 0].scatter(simulation.position[:, 0], simulation.position[:, 1], c=simulation.velocity[:, 0], s=0.75)
    ax[0, 1].scatter(simulation.position[:, 0], simulation.position[:, 1], c=simulation.pressure[:, 0], s=0.75)
    ax[0, 2].scatter(simulation.position[:, 0], simulation.position[:, 1], c=simulation.sdf[:, 0], s=0.75)
    ax[1, 0].scatter(simulation.position[:, 0], simulation.position[:, 1], c=simulation.nu_t[:, 0], s=0.75)
    ax[1, 1].scatter(simulation.airfoil_position[:, 0], simulation.airfoil_position[:, 1], c=simulation.airfoil_normals[:, 0], s=0.75)
    ax[1, 2].scatter(simulation.airfoil_position[:, 0], simulation.airfoil_position[:, 1], c=simulation.airfoil_normals[:, 1], s=0.75)

    # Add titles and labels
    ax[0, 0].set_title('Position vs. Velocity')
    ax[0, 0].set_xlabel('X Position')
    ax[0, 0].set_ylabel('Y Position')

    # Show the plot
    plt.show()