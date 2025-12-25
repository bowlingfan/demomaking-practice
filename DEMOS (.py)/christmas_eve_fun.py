# title:   christmas eve fun!
# author:  b0wling
# desc:    simple demo for the christmas blessing
# site:    https://extremities.neocities.org/
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python
import math
import random

# affects "everything"
class VariableManager:
    def __init__(self):
        self.tick = 0

        self.window_width = 240
        self.window_height = 136

        self.christmas_lights = []
        """
        data = [] for each "christmas lights":
        data[0] = ChristmasLights --> origin_y
        data[1] = ChristmasLights --> horizontal_stretch_factor
        """
        self.christmas_lights_configuration = [
            [9,11],
            [34,10],
            [51,15],
            [85,7],
            [109,13],
            [126,4],
        ]
        self.christmas_string_color = 0
        self.christmas_light_colors = [2,6,12]
        self.christmas_light_radius = 2
        self.christmas_light_displacement = 14
        self.christmas_light_offset = 3
        self.christmas_light_change_tick_min = 35
        self.christmas_light_change_tick_max = 100

        self.snowflakes = []
        self.snowflake_color = 13
        self.snowflake_tick_rate = 10
        self.snowflakes_limit = 50

        # in order
        self.messages = [
            "we love christmas spirit",
            "and hacking..",
            "have yourself a merry blessing",
            "and make sure to code!",
            "or ill hax your cookies :)",
            "merry christmas",
        ]
        self.message_color = 9
        self.message_index = 0
        self.message_current_tick = 0
        self.message_change_tick = 120
        self.message_origin_y = 68
        self.message_restart_delay_tick = 360 #6 seconds
        self.message_changing_lower = True
        self.message_changing_upper = False
        self.message_show = False

        self.circle_origin_size = 95
        self.circle_color = 10

variables = VariableManager()

class ChristmasLights:
    def __init__(self,origin_y,horizontal_stretch_factor):
        assert horizontal_stretch_factor != 0, "don't divide by 0."
        self.origin_y = origin_y
        self.horizontal_stretch_factor = horizontal_stretch_factor
        self.tick = 0
        self.light_change_tick = random.randint(variables.christmas_light_change_tick_min, variables.christmas_light_change_tick_max)
        self.light_colors = self.make_set_of_colors()
    def draw(self):
        self.draw_string()
        self.draw_lights()
    def increment_tick(self):
        self.tick += 1
        if self.tick%self.light_change_tick==0:
            self.light_colors = self.make_set_of_colors()
    def amt_of_christmas_lights(self):
        return variables.window_width//variables.christmas_light_displacement+1
    def make_set_of_colors(self):
        colors = []
        for _ in range(self.amt_of_christmas_lights()):
            colors.append(random.choice(variables.christmas_light_colors))
        return colors
    def draw_string(self):
        for i in range(variables.window_width):
            pix(i,self.origin_y+int(math.sin(i/self.horizontal_stretch_factor)*3),variables.christmas_string_color)
    def draw_lights(self):
        for i in range(self.amt_of_christmas_lights()):
            circ(i*variables.christmas_light_displacement,self.origin_y+int(math.sin((i*variables.christmas_light_displacement)/self.horizontal_stretch_factor)*3)+variables.christmas_light_offset,variables.christmas_light_radius,self.light_colors[i])
class Snowflake:
    def __init__(self):
        self.origin_x = random.randint(0,variables.window_width)
        self.y = -1
    def draw(self):
        circ(self.origin_x, self.y, 1, variables.snowflake_color)
def let_it_snow():
    if variables.tick%variables.snowflake_tick_rate == 0 and len(variables.snowflakes)<variables.snowflakes_limit:
        variables.snowflakes.append(Snowflake())
        variables.snowflakes.append(Snowflake())
    for snowflake in variables.snowflakes:
        snowflake.y += 1
        snowflake.draw()
    if len(variables.snowflakes)>=variables.snowflakes_limit:
        variables.snowflakes.pop(0)
def show_christmas_lights():
    for christmas_light in variables.christmas_lights:
        christmas_light.increment_tick()
        christmas_light.draw()
def show_message():
    msg_width = print(variables.messages[variables.message_index],0,-6)
    msg_actual_color = variables.message_color if variables.message_index != 4 else 3

    # should it be moving from the bottom to the middle?
    if variables.message_changing_lower:
        variables.message_current_tick += 1
        y = variables.window_height+6-variables.message_current_tick
        print(variables.messages[variables.message_index],120-(msg_width//2),y,msg_actual_color)
        if y <= variables.message_origin_y:
            variables.message_changing_lower = False
            variables.message_show = True
            variables.message_current_tick = 0
    # should it be moving from the middle to the top?
    elif variables.message_changing_upper:
        variables.message_current_tick += 1
        y = variables.message_origin_y-variables.message_current_tick
        print(variables.messages[variables.message_index],120-(msg_width//2),y,msg_actual_color)
        if y == -6:
            variables.message_changing_upper = False
            variables.message_index += 1
            if variables.message_index >= len(variables.messages):
                variables.message_index = 0
                variables.message_show = False
            else:
                variables.message_changing_lower = True
            variables.message_current_tick = 0
    # not moving; showing message
    elif variables.message_show:
        variables.message_current_tick += 1
        print(variables.messages[variables.message_index],120-(msg_width//2),variables.message_origin_y,msg_actual_color)
        if variables.message_current_tick>=variables.message_change_tick:
            variables.message_changing_upper=True
            variables.message_show = False
            variables.message_current_tick = 0
    # completely hidden
    else:
        variables.message_current_tick += 1
        if variables.message_current_tick >= variables.message_restart_delay_tick:
            variables.message_changing_lower=True
            variables.message_current_tick=0
        
def breathe_circle():
    radius = variables.circle_origin_size+int(math.sin(variables.tick/15)*2)*3
    circb(variables.window_width//2,variables.window_height//2,radius,variables.circle_color)
    circb(variables.window_width//2,variables.window_height//2,radius-1,variables.circle_color)
    circb(variables.window_width//2,variables.window_height//2,radius-2,variables.circle_color)
# main function
def BOOT():
    for data in variables.christmas_lights_configuration:
        variables.christmas_lights.append(ChristmasLights(data[0],data[1]))
def TIC():
    cls(8)
    show_christmas_lights()
    show_message()
    let_it_snow()
    breathe_circle()
    variables.tick+=1