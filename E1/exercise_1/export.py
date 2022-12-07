"""Export to disk"""


def export_mesh_to_obj(path, vertices, faces):
    """
    exports mesh as OBJ
    :param path: output path for the OBJ file
    :param vertices: Nx3 vertices
    :param faces: Mx3 faces
    :return: None
    """

    # write vertices starting with "v "
    # write faces starting with "f "

    # ###############
    # TODO: Implement

    file = open(path, "a")
    file.truncate(0)
    for vertex in vertices:
        for v in vertex:
            v_str = ' '.join(list(map(str, v)))
            new_vertices_line = 'v ' + v_str + '\n'
            # write to file
            file.write(new_vertices_line)
    for face_idx, face in enumerate(faces):
        face_str = ' '.join(list(map(str, face)))
        new_face_line = 'f ' + face_str + '\n'
        file.write(new_face_line)

    file.close()

    # ###############


def export_pointcloud_to_obj(path, pointcloud):
    """
    export pointcloud as OBJ
    :param path: output path for the OBJ file
    :param pointcloud: Nx3 points
    :return: None
    """

    # ###############
    # TODO: Implement
    file = open(path, "a")
    file.truncate(0)
    for point in pointcloud:
        for p_i in point:
            p_str = ' '.join(list(map(str, p_i)))
            new_vertices_line = 'v ' + p_str + '\n'
            file.write(new_vertices_line)
    file.close()
    # ###############
