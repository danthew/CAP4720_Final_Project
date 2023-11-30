from model import ExtendedBaseModel
import glm
import moderngl as mgl
import pygame as pg
from camera import Camera
from gui_stuff import GUI

FOV = 50
NEAR = 0.1
FAR = 100
SPEED = 0.01
ROTATION_SPEED = 0.1
SENSITIVITY = 0.05

class Car(ExtendedBaseModel):
    def __init__(self, app, vao_name = 'car', tex_id = 'car', pos = (0, 5, 0), rot = (0, 180, 0), scale = (1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.camera = Camera(self.app, (pos[0], pos[1] + 4, pos[2] + 12))

    def update_car(self):
        self.texture = self.app.mesh.texture.textures[self.app.gui.get_car_texture()]
        # self.program['shiny'].write(self.app.gui.get_shine())

    # def move(self):
    #     velocity = SPEED * self.app.delta_time
    #     swerve = ROTATION_SPEED * self.app.delta_time
    #     keys = pg.key.get_pressed()
    #     if keys[pg.K_w]:
    #         if keys[pg.K_a]:
    #             self.yaw -= swerve
    #             self.update_camera_vectors()
    #         # self.rotate()
    #         if keys[pg.K_d]:
    #             self.yaw += swerve
    #             self.update_camera_vectors()
    #         self.position += self.forward * velocity
    #     if keys[pg.K_s]:
    #         if keys[pg.K_a]:
    #             self.yaw -= swerve
    #             self.update_camera_vectors()
    #         # self.rotate()
    #         if keys[pg.K_d]:
    #             self.yaw += swerve
    #             self.update_camera_vectors()
    #         self.position -= self.forward * velocity