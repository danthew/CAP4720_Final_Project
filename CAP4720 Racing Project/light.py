import glm

class Light:
    def __init__(self, app, position = (3, 3, -3), color = (1, 1, 1)):
        self.app = app
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        self.direction = glm.vec3(0, 0, 0)
        # intensities
        self.Ia = 0.1 * self.color # ambient
        self.Id = 0.8 * self.color # diffuse
        self.Is = 1.0 * self.color # specular
        # view matrix
        self.m_view_light = self.get_view_matrix()

    def update(self):
        time_of_day = self.app.time_param
        if time_of_day == 'skybox':
            self.color = (1, 1, 1)
        else:
            self.color = (0.4, 0.4, 0.4)
        self.color = glm.vec3(self.color)
        self.Ia = 0.1 * self.color # ambient
        self.Id = 0.8 * self.color # diffuse
        self.Is = 1.0 * self.color # specular

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))