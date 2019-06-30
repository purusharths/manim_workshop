from manimlib.imports import *

class AddingNumberPlane(SpecialThreeDScene):
    def construct(self):
        grid = NumberPlane()
        circle = Circle(color=YELLOW)
        self.play(ShowCreation(grid))
        self.add_axes()
        self.play(ShowCreation(circle))


        # excercise: create a lambda function for a new non linear transfomation
        # Refer: next file
