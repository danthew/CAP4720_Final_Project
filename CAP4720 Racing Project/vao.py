from vbo import VBO
from shader_program import ShaderProgram
import moderngl

class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # car vao
        self.vaos['car'] = self.get_vao(
            program = self.program.programs['car'],
            vbo = self.vbo.vbos['car']
        )

        # track vao
        self.vaos['track'] = self.get_vao(
            program = self.program.programs['default'],
            vbo = self.vbo.vbos['track']
        )

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program = self.program.programs['default'],
            vbo = self.vbo.vbos['cube']
        )

        # # shadow cube vao
        # self.vaos['shadow_cube'] = self.get_vao(
        #     program = self.program.programs['shadow_map'],
        #     vbo = self.vbo.vbos['cube']
        # )

        # skybox vao
        # self.vaos['skybox'] = self.get_vao(
        #     program = self.program.programs['skybox'],
        #     vbo = self.vbo.vbos['skybox']
        # )

        # advanced skybox vao
        self.vaos['advanced_skybox'] = self.get_vao(
            program = self.program.programs['advanced_skybox'],
            vbo = self.vbo.vbos['advanced_skybox']
        )

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors = True)
        return vao
    
    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()