import pygame as pg
import moderngl as mgl
import sys
# from triangleModel import *
from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene
from scene_renderer import SceneRenderer
from gui_stuff import GUI
from movement_handler import MovementHandler

class GraphicsEngine:
    def __init__(self, win_size=(1200, 900)):
        # init pygame modules
        pg.init()
        # window size
        self.WIN_SIZE = win_size
        # set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags = pg.OPENGL | pg.DOUBLEBUF)
        # mouse settings
        # pg.event.set_grab(True)
        # pg.mouse.set_visible(False)
        # detect and use existing opengl context
        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw'
        self.ctx.enable(flags = mgl.DEPTH_TEST | mgl.CULL_FACE)
        # create time tracker obj
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # gui
        self.gui = GUI(self)
        # light
        self.light = Light(self)
        # camera
        self.camera = Camera(self)
        # movement handler IF NEEDED
        # self.mh = MovementHandler(self)
        # mesh
        self.mesh = Mesh(self)
        # scene
        self.scene = Scene(self)
        # renderer
        self.scene_renderer = SceneRenderer(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                # print(self.scene.car.pos)
                self.mesh.destroy()
                self.scene_renderer.destroy()
                pg.quit()
                sys.exit()
    
    def render(self):
        # clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        # # move car
        # self.movement_handler.move()
        # render scene
        self.scene_renderer.render()
        # swap buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.gui.update_gui()
            # GraphicsEngine.update_gui(self, self.interface)
            self.check_events()
            self.light.update()
            self.camera.update()
            # self.scene.car.camera.update()
            # self.mh.update()
            # self.scene.car.camera.update()
            self.render()
            # set fps to 60
            self.delta_time = self.clock.tick(60)

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()