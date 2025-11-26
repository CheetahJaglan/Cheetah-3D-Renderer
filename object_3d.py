from init import np, math,pygame
from matrix_functions import translate, rotate_x, rotate_y, rotate_z, scale



import numpy as np

class Object3D:
    def __init__(self, render, object_vertices, object_edges):
        self.render = render 

        self.vertices = object_vertices.copy()
        self.edges = object_edges.copy()

        



        # cube verts (homogeneous)


    def draw(self,shader):
        if shader == "wireframe":
            self.screen_projection_edges()
        elif shader == "vertex":
            self.screen_projection_vertex()  
        else:
            self.screen_projection_edges()
            self.screen_projection_vertex()      


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

    def screen_projection_edges(self):
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
            
    def screen_projection_vertex(self):
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

        # draw vertices
        for vert in verts:
            if np.any(vert == self.render.H_WIDTH):
                continue  # clipped
            
            pygame.draw.circle(self.render.screen, pygame.Color('red'),
                            tuple(vert.astype(int)), 5)
            
        
