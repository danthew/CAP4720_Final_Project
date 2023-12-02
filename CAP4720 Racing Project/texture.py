import pygame as pg
import moderngl as mgl

class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures['orange_car'] = self.get_texture(path = 'textures/orange_car.png')
        self.textures['purple_car'] = self.get_texture(path = 'textures/purple_car.png')
        self.textures['yellow_car'] = self.get_texture(path = 'textures/yellow_car.png')
        self.textures['green_car'] = self.get_texture(path = 'textures/green_car.png')
        self.textures['blue_car'] = self.get_texture(path = 'textures/blue_car.png')
        self.textures['pixel_car'] = self.get_texture(path = 'textures/pixel_grid.png')

        self.textures['number_1'] = self.get_texture(path = 'textures/number_1.png')
        self.textures['number_2'] = self.get_texture(path = 'textures/number_2.png')
        self.textures['number_3'] = self.get_texture(path = 'textures/number_3.png')
        self.textures['number_4'] = self.get_texture(path = 'textures/number_4.png')
        self.textures['number_5'] = self.get_texture(path = 'textures/number_5.png')
        self.textures['number_6'] = self.get_texture(path = 'textures/number_6.png')
        self.textures['number_7'] = self.get_texture(path = 'textures/number_7.png')
        self.textures['number_8'] = self.get_texture(path = 'textures/number_8.png')
        self.textures['number_9'] = self.get_texture(path = 'textures/number_9.png')
        self.textures['number_0'] = self.get_texture(path = 'textures/number_0.png')

        self.textures['cube'] = self.get_texture(path = 'textures/img.png')
        # self.textures['steel'] = self.get_texture(path = 'textures/img_1.png')
        self.textures['skybox'] = self.get_texture_cube(dir_path = 'textures/skybox1/', ext = 'png')
        self.textures['skybox2'] = self.get_texture_cube(dir_path = 'textures/skybox2/', ext = 'png')
        # self.textures['depth_texture'] = self.get_depth_texture()

    def get_depth_texture(self):
        depth_texture = self.ctx.depth_texture(self.app.WIN_SIZE)
        return depth_texture

    def get_texture_cube(self, dir_path, ext = 'png'):
        faces = ['right', 'left', 'top', 'bottom'] +  ['front', 'back'][::-1]
        # textures = [pg.image.load(dir_path + f'{face}.{ext}').convert() for face in faces]
        textures = []
        for face in faces:
            texture = pg.image.load(dir_path + f'{face}.{ext}').convert()
            if face in {'right', 'left', 'front', 'back'}:
                texture = pg.transform.flip(texture, flip_x = True, flip_y = False)
            else:
                texture = pg.transform.flip(texture, flip_x = False, flip_y = True)
            textures.append(texture)
        size = textures[0].get_size()
        texture_cube = self.ctx.texture_cube(size = size, components = 3, data = None)
        for i in range(6):
            texture_data = pg.image.tostring(textures[i], 'RGB')
            texture_cube.write(face = i, data = texture_data)
        return texture_cube

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x = False, flip_y = True)
        texture = self.ctx.texture(size = texture.get_size(),
                                   components = 3,
                                   data = pg.image.tostring(texture, 'RGB'))
        # mipmaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        # AF
        texture.anisotropy = 32.0
        return texture
    
    def destroy(self):
        [tex.release() for tex in self.textures.values()]