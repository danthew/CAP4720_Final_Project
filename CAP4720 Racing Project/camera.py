import glm
import pygame as pg

FOV = 50
NEAR = 0.1
FAR = 100
SPEED = 0.01
ROTATION_SPEED = 0.05
SENSITIVITY = 0.05
ACCELERATION = 0.005

class Camera:
    def __init__(self, app, position = (0, 0, 4), yaw = -90, pitch = 0):
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
        # view matrix
        self.m_view = self.get_view_matrix()
        self.m_proj = self.get_projection_matrix()

    # def rotate(self):
    #     rel_x, rel_y = pg.mouse.get_rel()
    #     # rel_x = -self.right * SPEED
    #     # rel_y = self.right * SPEED
    #     self.yaw += rel_x * SENSITIVITY
    #     # self.pitch -= rel_y * SENSITIVITY
    #     # self.pitch = max(-89, min(89, self.pitch))

    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        self.move()
        # self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

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
                self.update_camera_vectors()
            # self.rotate()
            if keys[pg.K_d]:
                self.yaw += swerve
                self.update_camera_vectors()
            self.position += self.forward * (velocity + self.current_accel)
        elif keys[pg.K_s]:
            self.last_key = 's'
            if self.current_accel > -velocity * 2:
                self.current_accel -= ACCELERATION
            if keys[pg.K_a]:
                self.yaw -= swerve
                self.update_camera_vectors()
            # self.rotate()
            if keys[pg.K_d]:
                self.yaw += swerve
                self.update_camera_vectors()
            self.position -= self.forward * (velocity - self.current_accel)
        else:
            if self.current_accel > 0:
                self.current_accel -= ACCELERATION
                # if self.last_key == 'w':
                self.position += self.forward * (velocity + self.current_accel)
            elif self.current_accel < 0:
                self.current_accel = 0
                # self.position -= self.forward * (velocity + self.current_accel)
                # elif self.last_key == 's':
                #     self.position -= self.forward * (velocity + self.current_accel)
            # elif self.current_accel < 0:
            #     self.current_accel += ACCELERATION
            #     # if self.last_key == 'w':
            #     # self.position += self.forward * (velocity + self.current_accel)
            #     # elif self.last_key == 's':
            #     self.position -= self.forward * (velocity + self.current_accel)
            else:
                pass
        
            # self.rotate()
        # if keys[pg.K_q]:
        #     self.position += self.up * velocity
        # if keys[pg.K_e]:
        #     self.position -= self.up * velocity
        

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)