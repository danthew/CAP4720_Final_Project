from model import ExtendedBaseModel
import pygame as pg
from camera import Camera
from gui_stuff import GUI

SPEED = 0.01

class Car(ExtendedBaseModel):
    def __init__(self, app, vao_name = 'car', tex_id = 'car', pos = (0, 5, 0), rot = (0, 180, 0), scale = (1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.camera = Camera(self.app, (pos[0], pos[1] + 4, pos[2] + 12))

    # def move(self):
    #     velocity = SPEED * self.app.delta_time
    #     keys = pg.key.get_pressed()
    #     if keys[pg.K_w]:
    #         self.pos.x += velocity
    #     if keys[pg.K_s]:
    #         self.pos.x -= velocity
    #     if keys[pg.K_a]:
    #         self.pos.y -= velocity
    #     if keys[pg.K_d]:
    #         self.pos.y += velocity