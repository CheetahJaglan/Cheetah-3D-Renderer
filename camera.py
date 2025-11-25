from init import pygame,np, math

from matrix_functions import translate, rotate_x, rotate_y, rotate_z, scale

class Camera:
    def __init__(self,render, position):
        self.render = render
        self.position = np.array([*position,1.0])
        self.forward = np.array([0,0,1,1])
        self.up = np.array([0,1,0,1])
        self.right = np.array([1,0,0,1])
        self.h_pov = math.pi / 3
        self.v_pov = self.h_pov * (render.HEIGHT / render.WIDTH)
        self.near_plane = 0.1
        self.far_plane = 100
    def translate_matrix(self):
        x,y,z,w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])
    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        ux, uy, uz, w = self.up
        fx, fy, fz, w = self.forward
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])
    def camera_matrix(self):
        return self.translate_matrix() @ self.rotate_matrix()

