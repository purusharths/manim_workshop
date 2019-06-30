from manimlib.imports import *

class DemoParametricFunctions(Scene):
    def construct(self):
        path = ParametricFunction(
            lambda t: np.array([
                -np.sin(t),
                np.cos(t),
                0
            ]),
            color=RED
        )
        self.play(ShowCreation(path))
        self.wait(2)
