"""Creating an SDF grid"""
import numpy as np


def sdf_grid(sdf_function, resolution):
    """
    Create an occupancy grid at the specified resolution given the implicit representation.
    :param sdf_function: A function that takes in a point (x, y, z) and returns the sdf at the given point.
    Points may be provides as vectors, i.e. x, y, z can be scalars or 1D numpy arrays, such that (x[0], y[0], z[0])
    is the first point, (x[1], y[1], z[1]) is the second point, and so on
    :param resolution: Resolution of the occupancy grid
    :return: An SDF grid of specified resolution (i.e. an array of dim (resolution, resolution, resolution) with positive values outside the shape and negative values inside.
    """

    # ###############
    # TODO: Implement
    coordinates = np.linspace(-0.5, 0.5, num=resolution)
    x, y, z = np.meshgrid(coordinates, coordinates, coordinates, indexing='ij')
    sdf_values = sdf_function(x.flatten(), y.flatten(), z.flatten())
    grid = sdf_values.reshape(resolution, resolution, resolution)

    return grid
    # ###############
