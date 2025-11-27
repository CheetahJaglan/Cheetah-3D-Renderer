from init import np

tri_pyramid_vertices = np.array([
    (0,   0,   0, 1),   # 0
    (1,   0,   0, 1),   # 1
    (0.5, 0,   0.866, 1),  # 2 (equilateral base)
    (0.5, 1,   0.288, 1)   # 3 apex centered above base
], dtype=float)

tri_pyramid_edges = np.array([
    (0, 1), (1, 2), (2, 0),  # base
    (0, 3), (1, 3), (2, 3)   # sides
], dtype=int)

tri_pyramid_faces = np.array([
    (0, 1, 2),  # base
    (0, 1, 3),  # sides
    (1, 2, 3),
    (2, 0, 3)
], dtype=int)
