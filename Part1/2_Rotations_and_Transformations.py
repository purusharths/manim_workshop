from manimlib.imports import *

class MoveToEx(Scene):
    def construct(self):
        square = Square() # creating circle mobject
        square.move_to(2*RIGHT+3*UP) # .move_to moves the circle mobject to coordinate: (2,3)
        self.play(ShowCreation(square))
        self.wait(2)

class ApplyMethodEx(Scene):
    def construct(self):
        square = Square() # creating circle mobject
        self.play(ShowCreation(square)) # create square mobject on scene
        self.play(ApplyMethod(square.move_to, 4*LEFT+3*DOWN)) # move the mobject
        self.wait(2)

class Sq_to_Cr(Scene):
    def construct(self):
        s1 = Square() # creating square mobject
        c1 = Circle() # creating circle mobject
        self.play(ShowCreation(s1))
        self.play(Transform(s1, c1)) # transforming s1 -> c1
        self.wait(2)
