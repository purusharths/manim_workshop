from manimlib.imports import *

def get_definition_text():
    return TextMobject(r"The number 'a' is said to be the limit of the", r"sequence ($y_n$)", r"""
                        if\\ for any positive number $\epsilon$ there exist a real number N, \\
                        such that for all $n \textgreater N$, the inequality $| y_n - a | \textless
                        \epsilon$ exists.""")

def get_custom_definition_text():
    custom_definition = TextMobject(r"The number", "5" ,"is said to be the limit of the",
                        r"sequence $15 \frac{(-1)^n}{n} + 5$",
                        r"if\\ for a positive number (say)", r"1 (arbitary $\epsilon$ value)\\",
                        r"there exist a real number", r"15, \\",
                        r"such that for all", r"$n \textgreater 15$", "the inequality",
                        r"$| y_n - 5 | \textless 1$", "exists.")
    custom_definition.scale(0.5)
    custom_definition.shift(3.3*RIGHT+3*UP)
    custom_definition.set_color_by_tex_to_color_map({r"sequence $15 \frac{(-1)^n}{n} + 5$": RED,
    "5":BLUE, r"15, \\": PINK,
    r"1 (arbitary $\epsilon$ value)\\":YELLOW,
    r"$n \textgreater 15$":ORANGE, r"$| y_n - 5 | \textless 1$": GREEN_C
    })

    return custom_definition

class IntroDefinitionText(Scene):
    def construct(self):
        definition = get_definition_text()
        title = TextMobject(r"Limit", "of a", "Sequence")

        definition.set_color_by_tex_to_color_map({"sequence ($y_n$)": YELLOW})
        title.shift(3 * UP)
        title.scale(1.5)
        title.set_color_by_tex_to_color_map({
            "Sequence": YELLOW,
            "Limit": BLUE
        })

        self.play(Write(definition))
        self.wait(4)
        self.play(ApplyMethod(definition.move_to, 1*DOWN))
        self.play(Write(title))
        self.wait(3)

        but_what_does_it_mean = TextMobject("But what does it mean?")
        self.play(ReplacementTransform(definition, but_what_does_it_mean))
        self.wait(2)
        self.play(FadeOut(but_what_does_it_mean), FadeOut(title))
        self.wait(1)


class ShowEquation(Scene):
    def construct(self):
        text = TextMobject("Consider the sequence")
        text.shift(1*UP)
        eqn = TextMobject(r"$15 \frac{(-1)^n}{n} + 5$")
        self.play(Write(text), Write(eqn))
        self.wait(2)

class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 30.3,
        "y_min": -10,
        "y_max": 10,
        "graph_origin": ORIGIN+4*LEFT,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$n$",
        "y_axis_label": "$y_n$",
        "exclude_zero_label": True,
        "x_labeled_nums": range(0, 31, 5),
        "y_labeled_nums": range(-10,10,2)
    }

    def get_text_limit(self, get_text = 1):
        if get_text == 1:
            lim = TextMobject("The limit of the given sequence is 5")
        if get_text == 2:
            lim = TextMobject(r"The arbitary value chosen for $\epsilon$ here is $1$")
        lim.shift(3*DOWN+1*RIGHT)
        lim.scale(0.7)
        return lim

    def construct(self):
        X_TICKS_DISTANCE = self.x_axis_width/(self.x_max - self.x_min)
        Y_TICKS_DISTANCE = self.y_axis_height / (self.y_max - self.y_min)
        epsilon = 1
        limit = 5
        n = 15

        self.setup_axes(animate=True) # sets up axis on the scene
        points = [ Dot(color = YELLOW, radius = 0.05) for dot in range(1,30) ]
        equation = TextMobject(r"$15 \frac{(-1)^n}{n} + 5$")
        equation.shift(3.3*RIGHT+3*UP)
        self.play(FadeIn(equation))

        mathfunc = lambda x: 15*((-1)**x)/x + 5
        [points[counter].shift(self.graph_origin + counter * (RIGHT * X_TICKS_DISTANCE) +
                               mathfunc(counter) * (UP * Y_TICKS_DISTANCE)) for counter in range(1,
                               len(points))]

        positive_epsilon = DashedLine(start = self.graph_origin, end=4.5*RIGHT, color=DARK_BROWN)
        positive_epsilon.shift(Y_TICKS_DISTANCE*(limit + epsilon)*UP)

        negative_epsilon = DashedLine(start=4 * LEFT, end=4.5 * RIGHT, color=DARK_BROWN)
        negative_epsilon.shift(Y_TICKS_DISTANCE * (limit - epsilon) * UP)

        limit_line = Line(start = self.graph_origin, end = 4.5 * RIGHT, color = LIGHT_BROWN)
        limit_line.shift(Y_TICKS_DISTANCE * limit * UP)

        for point in range(1,len(points)):
            self.add(points[point])
            self.wait(0.1)

        self.wait(2)

        definition = get_definition_text(); definition.scale(0.5); definition.shift(3.5*RIGHT+3.5*UP)
        formal_definition_notice = TextMobject("(Formal Definition)"); formal_definition_notice.scale(0.5)
        formal_definition_notice.shift(3.5*RIGHT+2.5*UP)
        custom_definition = get_custom_definition_text();

        epsilon_band = VGroup(positive_epsilon, negative_epsilon)

        self.play(ReplacementTransform(equation, definition)); self.wait(2)
        self.play(FadeIn(formal_definition_notice));self.wait(2)
        self.play(FadeOut(formal_definition_notice));self.wait(1)
        self.play(Transform(definition, custom_definition)); self.wait(2)

        # show text below graph
        lim = [self.get_text_limit(i) for i in range(1,3)]
        self.play(Write(lim[0])); self.wait(2)
        self.play(Transform(lim[0], limit_line))
        self.play(Write(lim[1])); self.wait(2)
        self.play(Transform(lim[1], epsilon_band))

        N_value = TextMobject("$N$")
        N_value.set_color_by_tex_to_color_map({"$N$":RED})
        N_value.shift(self.graph_origin + RIGHT*X_TICKS_DISTANCE*n + UP*(Y_TICKS_DISTANCE*mathfunc(n)-0.3))
        N_value.scale(0.8)
        N =  Dot(color = RED, radius = 0.1)
        N.shift(self.graph_origin + RIGHT*X_TICKS_DISTANCE*n + UP*Y_TICKS_DISTANCE*mathfunc(n))
        self.play(ShowCreation(N))
        self.play(ShowCreation(N_value))

        # for all n > N
        for_all_n_gt_N = TextMobject("For all", r"n \textgreater N")
        for_all_n_gt_N.set_color_by_tex_to_color_map({r"n \textgreater N":ORANGE})
        for_all_n_gt_N.scale(0.7); for_all_n_gt_N.shift(0.5*UP+2*RIGHT)
        self.play(Write(for_all_n_gt_N))
        more_dots = [ Dot(color = BLUE_A, radius = 0.06) for index in range(16,30)]
        [more_dots[counter].shift(self.graph_origin + (counter+15) * (RIGHT * X_TICKS_DISTANCE) +
                               mathfunc(counter+15) * (UP * Y_TICKS_DISTANCE)) for counter in range(1,14)]

        for point in range(1,len(more_dots)):
            self.add(more_dots[point])
            self.wait(0.2)
        self.wait(2)
        #self.play(FadeOut())


        band_rectangle = Rectangle(color=GOLD_B, color_opacity=0.2, fill_color=GOLD_B, fill_opacity=0.2,
                                    height=Y_TICKS_DISTANCE*2, width=X_TICKS_DISTANCE*30)
        band_rectangle.shift(self.graph_origin+X_TICKS_DISTANCE*RIGHT*15 + Y_TICKS_DISTANCE * UP*5)

        distance = TextMobject(r"""The distance between $y_n \textgreater N [y_{16}, y_{17} ...]$ and the limit, $5$, \\
                                remains inside the given band. \textit{i.e}\\
                                $| y_n - 5 | \textless 1$ for all $n \textgreater N$""")
        distance.scale(0.6)
        distance.shift(2.5*DOWN+1*RIGHT)
        self.play(Transform(for_all_n_gt_N, distance))

        #explanation1 = TextMobject(r"""All the values of the sequence from\\ $y_{16}$ (n \textgreater 15) onwards will lie inside this band""")
        #explanation1.scale(0.6)
        #explanation1.shift(2*DOWN+1*RIGHT)
        explanation2 = TextMobject(r"(Intutively) the sequence seems to be converging towards 5")
        explanation2.scale(0.6); explanation2.shift(3.5*DOWN+1*RIGHT)
        #Because for the given value of epsilion (\textit{i.e} 1), the value of N is 15""")
        self.play(ShowCreation(band_rectangle))
        self.wait(2)
        self.play(FadeIn(explanation2))
        self.wait(3)
