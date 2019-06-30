from manimlib.imports import *

class PlotFunctions(GraphScene):

    CONFIG = {
        "x_min" : -20,
        "x_max" : 20,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),
    }
    def construct(self):
        self.setup_axes(animate=False)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        func_graph2=self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)


        self.play(ShowCreation(func_graph),ShowCreation(func_graph2))
        self.wait(2)

    def func_to_graph(self,x):
        a = 4*np.sin(7*x)/7*np.pi
        return a

    def func_to_graph2(self,x):
        return np.sin(x)



# TODO: Add function labels!
