from init import np, math,pygame
from matrix_functions import translate, rotate_x, rotate_y, rotate_z, scale

class Object3D:
    def __init__(self, render):
        self.render = render
        self.vertices = np.array([
            (0, 0, 0, 1),
            (0, 1, 0, 1),
            (1, 1, 0, 1),
            (1, 0, 0, 1),
    
            (0, 0, 1, 1),
            (0, 1, 1, 1),
            (1, 1, 1, 1),
            (1, 0, 1, 1)
        ])
        self.edges = np.array([
            (0, 1), (1, 2), (2, 3), (3, 0),  # bottom square
            (4, 5), (5, 6), (6, 7), (7, 4),  # top square
            (0, 4), (1, 5), (2, 6), (3, 7)   # verticals
        ])

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
