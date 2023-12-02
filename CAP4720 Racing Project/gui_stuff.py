from guiV3 import SimpleGUI

class GUI:
    def __init__(self, app):
        self.app = app
        gui = SimpleGUI("Change Parameters")
        time_field = gui.add_radio_buttons("Time of Day", options_dict={'Day':'skybox', 'Night':'skybox2'}, initial_option='Day')
        # shiny_field = gui.add_slider("Shininess", min_value=5, max_value=66, initial_value=32, resolution=1)
        texture_field = gui.add_radio_buttons("Car Texture", options_dict={'Orange':'orange_car', 
                                                                           'Green':'green_car', 
                                                                           'Purple':'purple_car', 
                                                                           'Yellow':'yellow_car', 
                                                                           'Blue':'blue_car', 
                                                                           'Pixel':'pixel_car'})
        speed_field = gui.add_slider("Max Speed", min_value=1, max_value=5, initial_value=2, resolution=1)
        acceleration_field = gui.add_slider("Acceleration", min_value=0.002, max_value=0.01, initial_value=0.005, resolution=0.001)
        rotation_field = gui.add_slider("Steering Sensitivity", min_value=0.04, max_value=0.07, initial_value=0.05, resolution=0.01)
        self.interface = {}
        self.interface['time'] = time_field
        # self.interface['shiny'] = shiny_field
        self.interface['texture'] = texture_field
        self.interface['speed'] = speed_field
        self.interface['acceleration'] = acceleration_field
        self.interface['rotation'] = rotation_field
        self.update_gui()
        # return interface

    def update_gui(self):
        self.app.time_param = self.interface['time'].get_value()

    def get_car_texture(self):
        return self.interface['texture'].get_value()
    
    def get_max_speed(self):
        return self.interface['speed'].get_value()
    
    def get_acceleration(self):
        return self.interface['acceleration'].get_value()
    
    def get_rotation_speed(self):
        return self.interface['rotation'].get_value()
    
    # def get_shine(self):
    #     return self.interface['shiny'].get_value()