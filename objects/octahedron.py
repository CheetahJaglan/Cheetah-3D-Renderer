from init import np
octa_vertices = np.array([
    ( 0.0,  1.0,  0.0, 1),   # 0 top
    ( 0.5,  0.0,  0.0, 1),   # 1 right
    ( 0.0,  0.0,  0.5, 1),   # 2 front
    (-0.5,  0.0,  0.0, 1),   # 3 left
    ( 0.0,  0.0, -0.5, 1),   # 4 back
    ( 0.0, -1.0,  0.0, 1)    # 5 bottom
], dtype=float)

octa_edges = np.array([
    # top to mid ring
    (0, 1), (0, 2), (0, 3), (0, 4),

    # mid ring cycle
    (1, 2), (2, 3), (3, 4), (4, 1),

    # bottom to mid ring
    (5, 1), (5, 2), (5, 3), (5, 4)
], dtype=int)

octa_faces = np.array([
    # top pyramid
    (0, 1, 2),
    (0, 2, 3),
    (0, 3, 4),
    (0, 4, 1),

    # bottom pyramid
    (5, 2, 1),
    (5, 3, 2),
    (5, 4, 3),
    (5, 1, 4)
], dtype=int)
