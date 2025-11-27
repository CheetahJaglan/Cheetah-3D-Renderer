import numpy as np

vertices = np.array([
    (0, 0, 0, 1),
    (0, 1, 0, 1),
    (1, 1, 0, 1),
    (1, 0, 0, 1),

    (0, 0, 1, 1),
    (0, 1, 1, 1),
    (1, 1, 1, 1),
    (1, 0, 1, 1)
], dtype=float)

        # edges: pairs of vertex indices
edges = np.array([
    (0, 1), (1, 2), (2, 3), (3, 0),  # bottom square
    (4, 5), (5, 6), (6, 7), (7, 4),  # top square
    (0, 4), (1, 5), (2, 6), (3, 7)   # vertical edges
], dtype=int)

faces = np.array([
    (0, 1, 2, 3),  # bottom face
    (4, 5, 6, 7),  # top face
    (0, 1, 5, 4),  # side face
    (2, 3, 7, 6),  # side face
    (1, 2, 6, 5),  # side face
    (0, 3, 7, 4)   # side face
], dtype=int)