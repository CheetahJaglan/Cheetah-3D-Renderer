from init import np, math,pygame
from matrix_functions import translate, rotate_x, rotate_y, rotate_z, scale

import numpy as np

class Object3D:
    def __init__(self, render):
        self.render = render

        # cube verts (homogeneous)
        self.vertices = np.array([
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
        self.edges = np.array([
            (0, 1), (1, 2), (2, 3), (3, 0),  # bottom square
            (4, 5), (5, 6), (6, 7), (7, 4),  # top square
            (0, 4), (1, 5), (2, 6), (3, 7)   # vertical edges
        ], dtype=int)

    def draw(self):
        self.screen_projection()


    # ------------------------- TRANSFORMS -------------------------

    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)

    def scale(self, scale_to):
        self.vertices = self.vertices @ scale(scale_to)

    def rotate_x(self, angle):
        self.vertices = self.vertices @ rotate_x(angle)

    def rotate_y(self, angle):
        self.vertices = self.vertices @ rotate_y(angle)

    def rotate_z(self, angle):
        self.vertices = self.vertices @ rotate_z(angle)

    # ------------------------- PROJECTION + DRAW -------------------------

    def screen_projection(self):
        verts = self.vertices @ self.render.camera.camera_matrix()
        verts = verts @ self.render.projection.projection_matrix
        verts /= verts[:, -1].reshape(-1, 1)

        # quick out-of-NDC clip
        mask = (
            (verts[:, 0] > 2) | (verts[:, 0] < -2) |
            (verts[:, 1] > 2) | (verts[:, 1] < -2)
        )
        verts[mask, :2] = (self.render.H_WIDTH, self.render.H_HEIGHT)

        # convert to screen coords
        verts = verts @ self.render.projection.to_screen_matrix
        verts = verts[:, :2]

        # draw edges
        for a, b in self.edges:
            va = verts[a].astype(int)
            vb = verts[b].astype(int)

            if np.any(va == self.render.H_WIDTH) or np.any(vb == self.render.H_WIDTH):
                continue  # clipped

            pygame.draw.line(self.render.screen, pygame.Color('white'),
                         tuple(va), tuple(vb), 2)
