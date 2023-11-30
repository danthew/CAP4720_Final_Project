from model import *
from car_model import *
import pygame as pg
import sys

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = AdvancedSkybox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # floor
        n, s = 20, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s-4, z)))

        # # columns
        # for i in range(9):
        #     add(Cube(app, pos=(15, i * s, -9 + i), tex_id='cube'))
        #     add(Cube(app, pos=(15, i * s, 5 - i), tex_id='cube'))

        # # cat
        # add(Cat(app, pos=(5, -4, -10)))

        # moving cube
        self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex_id='steel')
        add(self.moving_cube)

        # self.car = Car(app, pos=(0, -1, -10), tex_id='car')
        self.car = Car(app, pos=(0, -1, -10), tex_id=self.app.gui.get_car_texture())
        add(self.car)

        # test obstacle
        add(Cube(app, pos=(5, -4.5, -10), tex_id='steel'))
        

    # def render(self):
    #     for obj in self.objects:
    #         obj.render()
    #     self.skybox.render()

    def update(self):
        self.moving_cube.rot.xyz = self.app.time
        self.skybox.update()
        # for obj in self.objects:
        #     obj.update()
        # self.car.update_shine()
        self.car.update_texture()