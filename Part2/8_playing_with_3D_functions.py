from manimlib.imports import *

class Special3DTransformation(SpecialThreeDScene):
    CONFIG = { # What does a CONFIG dictonary do?
        "camera_class": ThreeDCamera,
        "ambient_camera_rotation": None,
        "default_angled_camera_orientation_kwargs": {
            "phi": 70 * DEGREES,
            "theta": -135 * DEGREES,
            }
        }

    def construct(self):
        grid = NumberPlane()
        i_hat = Vector(direction=RIGHT, color=ORANGE)
        j_hat = Vector(direction=UP, color=RED)
        sphere = Sphere()
        circle = Circle(color=YELLOW)

        self.add(grid)
        self.add_axes()

        self.play(FadeIn(sphere))
        self.play(ShowCreation(circle), ShowCreation(i_hat), ShowCreation(j_hat))
        grid.prepare_for_nonlinear_transform()

        nonLinear_Transform = lambda p: p + np.array([p[0]**2, p[1]+p[0] ,p[0]*p[1]])

        self.play(grid.apply_function, nonLinear_Transform,
                  sphere.apply_function, nonLinear_Transform,
                  circle.apply_function, nonLinear_Transform,
                  i_hat.apply_function, nonLinear_Transform,
                  j_hat.apply_function, nonLinear_Transform, run_time=4)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(30)

    def add_axes(self):
        axes = self.axes = self.get_axes()
        axes.set_stroke(width=0.5)
        self.add(axes)
        # Orient
        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-110 * DEGREES,
        )
        self.begin_ambient_camera_rotation()
