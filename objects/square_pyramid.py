from init import np
sq_pyramid_vertices = np.array([
    (0,   0, 0, 1),  # 0
    (1,   0, 0, 1),  # 1
    (1,   0, 1, 1),  # 2
    (0,   0, 1, 1),  # 3
    (0.5, 1, 0.5, 1) # 4 apex
], dtype=float)

sq_pyramid_edges = np.array([
    (0, 1), (1, 2), (2, 3), (3, 0),  # base
    (0, 4), (1, 4), (2, 4), (3, 4)   # sides
], dtype=int)

sq_pyramid_faces = [
    (0, 1, 2, 3),  # base quad

    (0, 1, 4),     # side triangles
    (1, 2, 4),
    (2, 3, 4),
    (3, 0, 4)
]
