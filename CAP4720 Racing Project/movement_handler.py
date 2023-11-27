import moderngl as mgl
import numpy as np
import glm
import pygame as pg

class MovementHandler:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.mesh = app.mesh
        self.scene = app.scene

    def move(self):
        movement_vector = {}
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_W:
                    movement_vector.x = 1
                elif event.key == pg.K_S:
                    movement_vector.x = -1
                if event.key == pg.K_A:
                    movement_vector.y = -1
                elif event.key == pg.K_D:
                    movement_vector.y = 1
        return movement_vector