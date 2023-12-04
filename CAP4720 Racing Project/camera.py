import glm
import pygame as pg
import collision_handler as ch

FOV = 50
NEAR = 0.1
FAR = 1000
SPEED = 0.01
# ROTATION_SPEED = 0.05
SENSITIVITY = 0.05
# ACCELERATION = 0.005

class Camera:
    def __init__(self, app, position = (0, 0, 4), yaw = -90, pitch = 0):
        self.app = app
        # self.movement_handler = MovementHandler(self.app, position)
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]

        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch

        self.max_speed = 2.0
        self.max_acceleration = 0.005
        self.rotation_speed = 0.05
        self.current_accel = 0.0
        self.last_key = ''

        # view matrix
        self.m_view = self.get_view_matrix()
        self.m_proj = self.get_projection_matrix()

        self.collision_handler = ch.Collider(self)

    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        self.max_speed = self.app.gui.get_max_speed()
        self.max_acceleration = self.app.gui.get_acceleration()
        self.rotation_speed = self.app.gui.get_rotation_speed()
        self.move()
        # self.movement_handler.move()
        # self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

    def move(self):

        if self.collision_handler.car_track_collision():
             self.position -= self.forward * 5
             self.current_accel = 0
             return


        velocity = SPEED * self.app.delta_time
        swerve = self.rotation_speed * self.app.delta_time
        keys = pg.key.get_pressed()
        if abs(self.current_accel) > 0.01:
            if keys[pg.K_a]:
                    self.yaw -= swerve
                    self.update_camera_vectors()
            # self.rotate()
            elif keys[pg.K_d]:
                self.yaw += swerve
                self.update_camera_vectors()
        if keys[pg.K_w]:
            self.last_key = 'w'
            if self.current_accel < velocity * self.max_speed:
                # self.current_accel += ACCELERATION
                self.current_accel += self.max_acceleration
            self.position += self.forward * (velocity + self.current_accel)
        elif keys[pg.K_s]:
            self.last_key = 's'
            if self.current_accel > -velocity * self.max_speed:
                # self.current_accel -= ACCELERATION
                self.current_accel -= self.max_acceleration
            self.position += self.forward * (-velocity + self.current_accel)
        else:
            if self.current_accel > 0.01:
                # self.current_accel -= ACCELERATION
                self.current_accel -= self.max_acceleration
                # if self.last_key == 'w':
                self.position += self.forward * (velocity + self.current_accel)
            elif self.current_accel < -0.01:
                # self.current_accel = 0
                # self.current_accel += ACCELERATION
                self.current_accel += self.max_acceleration
                self.position += self.forward * (-velocity + self.current_accel)
            else:
                self.current_accel = 0
                pass
        

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)
        # return glm.lookAt(self.movement_handler.position, self.movement_handler.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)