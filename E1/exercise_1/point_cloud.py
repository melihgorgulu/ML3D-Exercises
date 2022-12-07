"""Triangle Meshes to Point Clouds"""
import numpy as np


def sample_point_cloud(vertices, faces, n_points):
    """
    Sample n_points uniformly from the mesh represented by vertices and faces
    :param vertices: Nx3 numpy array of mesh vertices
    :param faces: Mx3 numpy array of mesh faces
    :param n_points: number of points to be sampled
    :return: sampled points, a numpy array of shape (n_points, 3)
    """

    # ###############
    # TODO: Implement
    areas = []
    for face in faces:
        try:
            [c1, c2, c3] = vertices[face]
        except:
            #print("Face:", face)
            #print(vertices.shape)
            break
        areas.append(0.5*np.linalg.norm(np.cross(c2-c1, c3-c1)))
    areas = np.asarray(areas)
    probs = areas/areas.sum()
    rand_indices = np.random.choice(range(len(areas)), size=n_points, p=probs)

    sampled_points = []
    for face_index in rand_indices:
        [A, B, C] = vertices[faces[face_index]]
        [r1, r2] = np.random.rand(2)
        u = 1 - np.sqrt(r1)
        v = np.sqrt(r1)*(1-r2)
        w = np.sqrt(r1)*r2
        p = u*A + v*B + w*C
        sampled_points.append(p)
    return np.asarray(sampled_points)
    # ###############

