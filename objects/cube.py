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