from manimlib.imports import *

class AddingNumberPlane(SpecialThreeDScene):
    def construct(self):
        grid = NumberPlane()
        circle = Circle(color=YELLOW)
        self.play(ShowCreation(grid))
        self.add_axes()
        self.play(ShowCreation(circle))

        # excercise solution
        grid.prepare_for_nonlinear_transform()
        transformation_ =  lambda p: p + np.array([
            np.sin(p[1]),
            np.sin(p[0]),
            0])

        self.play(grid.apply_function, transformation_,
              circle.apply_function, transformation_)
