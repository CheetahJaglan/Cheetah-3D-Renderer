from init import *
from camera import Camera
from projection import Projection
from object_3d import Object3D

class SoftwareRender:
    def __init__(self):
        pygame.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600,900
        self.H_WIDTH, self.H_HEIGHT  = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pygame.display.set_mode(self.RES)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("3D Rendering Software | CHEETAH JAGLAN  " )
        self.create_objects()

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (30, 30, 30), (0, self.HEIGHT-20, self.WIDTH, 20))
        pygame.draw.rect(self.screen, (255,255,255), (0, self.HEIGHT-23,self.WIDTH , 3))
        self.screen.blit(pygame.font.SysFont("arial", 15).render(f"FPS : {str(int(self.clock.get_fps()))}", True, (120, 120, 120)),(10, self.HEIGHT-18))
        self.object.draw()
        # Drawing logic goes here
    def create_objects(self):
        self.camera = Camera(self, (0.5, 1, -4))
        self.projection = Projection(self)
        self.object = Object3D(self)
    def run(self):
        while True:
            self.draw()
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
            pygame.display.flip()
            self.clock.tick(self.FPS)



if __name__ == "__main__":
    renderer = SoftwareRender()
    renderer.run()