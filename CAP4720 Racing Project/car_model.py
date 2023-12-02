from model import ExtendedBaseModel
from model import Cube
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
        self.camera = Camera(self.app, (pos[0], pos[1] + 4, pos[2] + 15))
        # self.movement_handler = MovementHandler(self.app, position=pos)
        self.midway = False
        self.start_time = pg.time.get_ticks()
        self.best_time = 0.0
        self.time_holder = 0.0

    def update_car(self):
        self.texture = self.app.mesh.texture.textures[self.app.gui.get_car_texture()]
        self.m_model = self.get_model_matrix()
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # self.update()
        self.render()
        self.check_pos()
        # self.program['shiny'].write(self.app.gui.get_shine())

    def check_pos(self):
        self.time_holder = pg.time.get_ticks() - self.start_time
        if (self.app.camera.position[0] <= -80) & (self.app.camera.position[2] >= -10):
            self.midway = True
        if self.midway == True:
            if (self.app.camera.position[0] >= -80) & (self.app.camera.position[2] <= -10):
                if (self.time_holder < self.best_time) | (self.best_time == 0):
                    self.best_time = self.time_holder
                    self.time_holder = 0.0
                    self.app.scene.number_cube_best_time_1.update_number(((self.best_time % 60000) / 10000) % 10)
                    self.app.scene.number_cube_best_time_2.update_number(((self.best_time % 60000) / 1000) % 10)
                    self.app.scene.number_cube_best_time_3.update_number((self.best_time / 100) % 10)
                    # print(self.best_time)
                    self.midway = False
                self.start_time = pg.time.get_ticks()