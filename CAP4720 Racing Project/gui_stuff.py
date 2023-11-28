from guiV3 import SimpleGUI

class GUI:
    def __init__(self):
        gui = SimpleGUI("Change Parameters")
        time_field = gui.add_radio_buttons("Time of Day", options_dict={'Day':0, 'Night':1}, initial_option='Day')
        shiny_field = gui.add_slider("Shininess", min_value=5.0, max_value=66.0, initial_value=32.0)
        self.interface = {}
        self.interface['time'] = time_field
        self.interface['shiny'] = shiny_field
        # return interface

    def update_gui(car):
        # self.program['FOV'] = 
        # self.program['time'] = interface['time'].get_value()
        car.program['shiny'] = car.interface['shiny'].get_value()
        # self.program['MAX_STEPS'] = interface['steps'].get_value()
        # self.program['MAX_DIST'] = interface['dist'].get_value()
        # self.program['EPSILON'] = interface['epsilon'].get_value()
        # self.program['orbColor'] = interface['color'].get_color()
        # self.program['shadows'] = interface['shadows'].get_value()