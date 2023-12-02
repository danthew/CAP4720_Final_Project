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
        add(Track(self.app, pos = (0, -4.5, -10)))
        # add(Cube(app, pos = (0, 0, 0), scale = (1, 100, 5)))
        self.car = Car(app, pos=(0, -1, -10), tex_id=self.app.gui.get_car_texture())
        add(self.car)

    def update(self):
        self.skybox.update()
        self.car.update_car()