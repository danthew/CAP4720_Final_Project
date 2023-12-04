from model import *
from vbo import *
import camera

import math
import numpy as np
import glm
import pygame as pg
import pywavefront

SCALE = 10

class Collider:
    def __init__(self, camera):
        self.car_cam = camera
        self.track = pywavefront.Wavefront('objects/RaceTrack2.obj')
        self.track_vertices = self.track.vertices

        #print(type(track))
        #print(type(track_vertices))

        # selects only the vertices that are on the top of the track wall
        self.top_vertices = filter(lambda x: abs(x[1] - 2.3137) < 0.001, self.track_vertices)
        self.top_vertices_2d = [(v[0],v[2]) for v in self.top_vertices]

        #print(top_vertices_2d)

        self.top_rects = [pg.Rect(v[0]*SCALE-SCALE, (v[1]-10)*SCALE-SCALE, 2*SCALE, 2*SCALE) for v in self.top_vertices_2d]

        '''
        for rect in self.top_rects:
            print(rect)
        '''
    

    '''
    creates 2D version of the track (list of rectangles) and car (4 points representing the corners) 
    then checks for collision
    '''
    def car_track_collision(self) -> bool:
        

        car_pos = self.car_cam.position + glm.vec3(15*math.cos(math.radians(self.car_cam.yaw)),
                                                    0,
                                                    15*math.sin(math.radians(self.car_cam.yaw)))
        
        car_pos_2d = (car_pos[0]*SCALE, car_pos[2]*SCALE)

        #print(f'camera: {self.car_cam.position}')
        #print(f'car: {car_pos_2d}')

        for rect in self.top_rects:
            if (rect.collidepoint(car_pos_2d[0], car_pos_2d[1])):
                #print("COLLIDE")
                #print(f'rect: {rect} car_pos: {car_pos_2d}')
                return True



        return False