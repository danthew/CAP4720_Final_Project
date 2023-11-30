from guiV3 import SimpleGUI

class GUI:
    def __init__(self, app):
        self.app = app
        gui = SimpleGUI("Change Parameters")
        time_field = gui.add_radio_buttons("Time of Day", options_dict={'Day':'skybox', 'Night':'skybox2'}, initial_option='Day')
        shiny_field = gui.add_slider("Shininess", min_value=5, max_value=66, initial_value=32, resolution=1)
        texture_field = gui.add_radio_buttons("Car Texture", options_dict={'Orange':'orange_car', 
                                                                           'Green':'green_car', 
                                                                           'Purple':'purple_car', 
                                                                           'Yellow':'yellow_car', 
                                                                           'Blue':'blue_car'})
        self.interface = {}
        self.interface['time'] = time_field
        self.interface['shiny'] = shiny_field
        self.interface['texture'] = texture_field
        self.update_gui()
        # return interface

    def update_gui(self):
        # self.program['FOV'] = 
        # self.program['time'] = interface['time'].get_value()
        # self.app.shininess = self.interface['shiny'].get_value()
        self.app.time_param = self.interface['time'].get_value()
        # self.app.car_texture = self.interface['texture'].get_value()
        # self.program['MAX_STEPS'] = interface['steps'].get_value()
        # self.program['MAX_DIST'] = interface['dist'].get_value()
        # self.program['EPSILON'] = interface['epsilon'].get_value()
        # self.program['orbColor'] = interface['color'].get_color()
        # self.program['shadows'] = interface['shadows'].get_value()

    def get_car_texture(self):
        return self.interface['texture'].get_value()
    
    def get_shine(self):
        return self.interface['shiny'].get_value()