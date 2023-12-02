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

        # in case track doesn't work
        # add(Cube(app, pos = (0, -6, 0), scale = (60, 100, 1)))

        # track
        add(Track(app, pos = (0, -4.5, -10)))
        # add(Cube(app, pos = (0, 0, 0), scale = (1, 100, 5)))
        self.car = Car(app, pos=(0, -4, -10), tex_id=self.app.gui.get_car_texture())
        add(self.car)

        self.number_cube_current_time_1 = NumberCube(app, pos = (-2, 2, -10), tex_id="number_1", scale = (0.7, 0.7, 0.7))
        self.number_cube_current_time_1.camera = self.car.camera
        add(self.number_cube_current_time_1)

        self.number_cube_current_time_2 = NumberCube(app, pos = (0, 2, -10), tex_id="number_2", scale = (0.7, 0.7, 0.7))
        self.number_cube_current_time_2.camera = self.car.camera
        add(self.number_cube_current_time_2)

        self.number_cube_decimal = NumberCube(app, pos = (1, 1.5, -10), tex_id="number_0", scale = (0.1, 0.1, 0.1))
        self.number_cube_decimal.camera = self.car.camera
        add(self.number_cube_decimal)

        self.number_cube_current_time_3 = NumberCube(app, pos = (2, 2, -10), tex_id="number_3", scale = (0.7, 0.7, 0.7))
        self.number_cube_current_time_3.camera = self.car.camera
        add(self.number_cube_current_time_3)

        self.number_cube_best_time_1 = NumberCube(app, pos = (-2, 5, -10), tex_id="number_0", scale = (0.7, 0.7, 0.7))
        self.number_cube_best_time_1.camera = self.car.camera
        add(self.number_cube_best_time_1)

        self.number_cube_best_time_2 = NumberCube(app, pos = (0, 5, -10), tex_id="number_0", scale = (0.7, 0.7, 0.7))
        self.number_cube_best_time_2.camera = self.car.camera
        add(self.number_cube_best_time_2)

        self.number_cube_best_decimal = NumberCube(app, pos = (1, 5, -10), tex_id="number_0", scale = (0.1, 0.1, 0.1))
        self.number_cube_best_decimal.camera = self.car.camera
        add(self.number_cube_best_decimal)

        self.number_cube_best_time_3 = NumberCube(app, pos = (2, 5, -10), tex_id="number_0", scale = (0.7, 0.7, 0.7))
        self.number_cube_best_time_3.camera = self.car.camera
        add(self.number_cube_best_time_3)
        # add(Cube(app, pos = (-95, -2.5, -10)))

    def update(self):
        self.skybox.update()
        self.car.update_car()
        self.number_cube_current_time_1.update_number(((self.car.time_holder % 60000) / 10000) % 10)
        self.number_cube_current_time_2.update_number(((self.car.time_holder % 60000) / 1000) % 10)
        self.number_cube_current_time_3.update_number((self.car.time_holder / 100) % 10)
        # self.number_cube_current_time_1.update_number(8)
        # self.car.program['shiny'].write(self.app.gui.get_shine())