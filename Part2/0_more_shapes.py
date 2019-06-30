from manimlib.imports import *

class MoreShapes(Scene):
    def construct(self):
        # creating the objects
        circle = Circle()
        square = Square(fill_color=ORANGE, fill_opacity=1, color=GOLD_A)
        rectangle = Rectangle(height=2, width=3)
        ellipse = Ellipse(width=3, height=1, color=RED)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=PINK)

        # changing location of the objects created above
        square.move_to(UP+LEFT)
        circle.surround(square)
        ellipse.shift(2*DOWN+2*RIGHT)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)

        # adding all the objects to scene
        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse))
