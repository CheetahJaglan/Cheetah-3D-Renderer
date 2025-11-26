from init import *
from camera import Camera
from projection import Projection
from object_3d import Object3D

class SoftwareRender:
    def __init__(self):

        self.RES = self.WIDTH, self.HEIGHT = 1600,900
        self.H_WIDTH, self.H_HEIGHT  = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60


        print("")
        print("")

        print("Please enter the shape you want to render: ")
        print("1. Cube")
        print("2. Tetrahedron")
        print("3. Square Pyramid")
        print("4. Octahedron")
        shape_choice = input("Enter the number corresponding to your choice: ")
        if shape_choice == '1':
            from objects.cube import vertices, edges
            self.create_objects(vertices, edges)
        elif shape_choice == '2':
            from objects.tetrahedron import tri_pyramid_vertices, tri_pyramid_edges
            self.create_objects(tri_pyramid_vertices, tri_pyramid_edges)
        elif shape_choice == '3':
            from objects.square_pyramid import sq_pyramid_vertices, sq_pyramid_edges
            self.create_objects(sq_pyramid_vertices, sq_pyramid_edges)
        elif shape_choice == '4':
            from objects.octahedron import octa_vertices, octa_edges
            self.create_objects(octa_vertices, octa_edges)
        else:
            print("Invalid choice. Defaulting to Cube.")
            from objects.cube import vertices, edges
            self.create_objects(vertices, edges)


        print("")
        print("")

        print("Please choose the shader mode:")
        print("1. Wireframe")
        print("2. Vertex")
        print("3. Both")
        shader_choice = input("Enter the number corresponding to your choice: ")
        if shader_choice == '1':
            self.shader = "wireframe"
        elif shader_choice == '2':
            self.shader = "vertex"
        elif shader_choice == '3':
            self.shader  = "both"
        else:
            print("Invalid choice. Defaulting to normal mode.")
            self.shader = "both"



        pygame.init()
        self.screen = pygame.display.set_mode(self.RES)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("3D Rendering Software | CHEETAH JAGLAN  " )



    def draw(self):
        self.screen.fill((0, 0, 0))
        self.object.draw(shader=self.shader)  
        pygame.draw.rect(self.screen, (30, 30, 30), (0, self.HEIGHT-20, self.WIDTH, 20))
        pygame.draw.rect(self.screen, (255,255,255), (0, self.HEIGHT-23,self.WIDTH , 3))
        self.screen.blit(pygame.font.SysFont("arial", 15).render(f"FPS : {str(int(self.clock.get_fps()))}", True, (120, 120, 120)),(10, self.HEIGHT-18))

        # Drawing logic goes here

    def create_objects(self, vertices, edges):
        self.camera = Camera(self, (0.5, 1, -4))
        self.projection = Projection(self)
        self.object = Object3D(self, vertices, edges)

    def run(self):
        while True:
            self.draw()
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
            self.camera.control()
            pygame.display.flip()
            self.clock.tick(self.FPS)



if __name__ == "__main__":
    renderer = SoftwareRender()
    renderer.run()