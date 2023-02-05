import math
from py3d.physics.Collision import Collision
from py3d.core_ext.object3d import Object3D


class MovementRig(Object3D):
    """
    Add moving forwards and backwards, left and right, up and down (all local translations),
    as well as turning left and right, and looking up and down
    """
    def __init__(self, units_per_second=8, degrees_per_second=60,mouse_speed=20):
        # Initialize base Object3D.
        # Controls movement and turn left/right.
        super().__init__()
        self._mouse_speed = mouse_speed
        # Initialize attached Object3D; controls look up/down
        self._look_attachment = Object3D()
        self.children_list = [self._look_attachment]
        self._look_attachment.parent = self
        # Control rate of movement
        self._units_per_second = units_per_second
        self._degrees_per_second = degrees_per_second

        # Customizable key mappings.
        # Defaults: W, A, S, D, R, F (move), Q, E (turn), T, G (look)
        self.KEY_MOVE_FORWARDS = "w"
        self.KEY_MOVE_BACKWARDS = "s"
        self.KEY_MOVE_LEFT = "a"
        self.KEY_MOVE_RIGHT = "d"
        self.KEY_MOVE_UP = "r"
        self.KEY_MOVE_DOWN = "f"
        self.KEY_TURN_LEFT = "q"
        self.KEY_TURN_RIGHT = "e"
        self.KEY_LOOK_UP = "t"
        self.KEY_LOOK_DOWN = "g"
        self.KEY_SPACE = "space"
        self.KEY_SHIFT = "left shift"

    # Adding and removing objects applies to look attachment.
    # Override functions from the Object3D class.
    def add(self, child):
        self._look_attachment.add(child)

    def remove(self, child):
        self._look_attachment.remove(child)

    def update(self, input_object, delta_time,camera,list):
        move_amount = self._units_per_second * delta_time
        rotate_amount = self._degrees_per_second * (math.pi / 180) * delta_time
        rotate_amount_mouse = 10
        if input_object.is_key_pressed(self.KEY_MOVE_FORWARDS):
            self.translate(0, 0, -move_amount)
            if(Collision().check(camera,list)):
                self.translate(0, 0, move_amount)

        if input_object.is_key_pressed(self.KEY_MOVE_BACKWARDS):
            self.translate(0, 0, move_amount)
            if(Collision().check(camera,list)):
                self.translate(0, 0, -move_amount)

        if input_object.is_key_pressed(self.KEY_MOVE_LEFT):
            self.translate(-move_amount, 0, 0)
            if(Collision().check(camera,list)):
                self.translate(move_amount, 0, 0)

        if input_object.is_key_pressed(self.KEY_MOVE_RIGHT):
            self.translate(move_amount, 0, 0)
            if(Collision().check(camera,list)):
                self.translate(-move_amount, 0, 0)

        if input_object.is_key_pressed(self.KEY_MOVE_UP):
            self.translate(0, move_amount, 0)
            if(Collision().check(camera,list)):
                self.translate(0, -move_amount, 0)

        if input_object.is_key_pressed(self.KEY_MOVE_DOWN):
            self.translate(0, -move_amount, 0)
            if(Collision().check(camera,list)):
                self.translate(0, move_amount, 0)

        if input_object.is_key_pressed(self.KEY_TURN_RIGHT):
            self.rotate_y(-rotate_amount)
        if input_object.is_key_pressed(self.KEY_TURN_LEFT):
            self.rotate_y(rotate_amount)
        if input_object.is_key_pressed(self.KEY_LOOK_UP):
            self._look_attachment.rotate_x(rotate_amount)
        if input_object.is_key_pressed(self.KEY_LOOK_DOWN):
            self._look_attachment.rotate_x(-rotate_amount)
        if input_object._mouse_move != (0,0):
            self.rotate_y(-input_object._mouse_move[0]*self._mouse_speed*0.0001)
            self._look_attachment.rotate_x(-input_object._mouse_move[1]*self._mouse_speed*0.0001)
            input_object._mouse_move=(0,0)
        if input_object.is_key_pressed(self.KEY_SPACE):
            self.translate(0, move_amount, 0)
            if(Collision().check(camera,list)):
                self.translate(0, -move_amount, 0)
        if input_object.is_key_pressed(self.KEY_SHIFT):
            self.translate(0, -move_amount, 0)
            if(Collision().check(camera,list)):
                self.translate(0, move_amount, 0)



