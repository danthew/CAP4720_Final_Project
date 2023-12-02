from model import ExtendedBaseModel
import glm
import moderngl as mgl
import pygame as pg
from camera import Camera
from gui_stuff import GUI
from movement_handler import MovementHandler

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