import glm
import pygame as pg

FOV = 50
NEAR = 0.1
FAR = 100
SPEED = 0.01
ROTATION_SPEED = 0.05
SENSITIVITY = 0.05
ACCELERATION = 0.005

class MovementHandler:
    def __init__(self, app, position=(0, 0, 0), yaw = -90, pitch = 0):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch
        self.current_accel = 0.0
        self.last_key = ''

    def update(self):
        self.move()
        
    def move(self):
        velocity = SPEED * self.app.delta_time
        swerve = ROTATION_SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.last_key = 'w'
            if self.current_accel < velocity * 2:
                self.current_accel += ACCELERATION
            if keys[pg.K_a]:
                self.yaw -= swerve
                # self.update_camera_vectors()
            # self.rotate()
            if keys[pg.K_d]:
                self.yaw += swerve
                # self.update_camera_vectors()
            self.position += self.forward * (velocity + self.current_accel)
        elif keys[pg.K_s]:
            self.last_key = 's'
            if self.current_accel > -velocity * 2:
                self.current_accel -= ACCELERATION
            if keys[pg.K_a]:
                self.yaw -= swerve
                # self.update_camera_vectors()
            # self.rotate()
            if keys[pg.K_d]:
                self.yaw += swerve
                # self.update_camera_vectors()
            self.position += self.forward * (-velocity + self.current_accel)
        else:
            if self.current_accel > 0.0:
                self.current_accel -= ACCELERATION
                # if self.last_key == 'w':
                self.position += self.forward * (velocity + self.current_accel)
            elif self.current_accel < 0.0:
                # self.current_accel = 0
                self.current_accel += ACCELERATION
                self.position += self.forward * (-velocity + self.current_accel)
            else:
                pass