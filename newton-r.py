from manim import *
import numpy as np
from sympy import *  

def stopCritterion(p_0: 'float', p_1: 'float', eps: 'float') -> 'bool':
    if abs(p_1 - p_0) >= eps:
        return False
    else: return True

def newton_R(p_0, f, iterations, eps):
    x_points = [p_0]
    y_points = []
    deriv = []
    f_diff = lambdify(Symbol('x'), f(Symbol('x')).diff(Symbol('x')), 'numpy')

    for i in range(0, iterations):
        y = float(f(p_0))

        evalu = y
        dv = f_diff(p_0)


        deriv.append(dv)
        y_points.append(evalu)

        p = p_0 - evalu/dv
        
        if stopCritterion(p_0, p, eps):
            break
        p_0 = p
        x_points.append(p)
    return x_points, y_points, deriv

class Newton_R(Scene):
    def __init__(self, func, iterations, eps, p_0):
        super().__init__()
        self.function_2exec = func
        self.iterations = iterations
        self.eps = eps
        self.p_0 = p_0

    def construct(self):
        x_lim = max(self.p_0, -self.p_0)
        y_lim = max(float(self.function_2exec(self.p_0)), -float(self.function_2exec(self.p_0)))
        axtick_ref = min(x_lim, y_lim)
        axes = Axes(x_range = [-x_lim*2, x_lim*2, (2*2*axtick_ref)/2], y_range = [-y_lim*2, y_lim*2, (2*2*axtick_ref)/2],
        axis_config = {"numbers_to_exclude": [0], "include_numbers": False, "stroke_width": 0.5, "include_ticks": False}, tips = False)
        
        axis_labels = axes.get_axis_labels(x_label = "x", y_label = "f(x)")

        graph = axes.plot(self.function_2exec, x_range=[-x_lim*2, x_lim*2], use_smoothing=True)
        self.add(axes, graph)
        graphing_stuff = VGroup(axes, graph, axis_labels)

        x_points, y_points, deriv = newton_R(self.p_0, self.function_2exec, self.iterations, self.eps)

        self.play(Create(graph), run_time = 2)
        
        self.wait()
        for x_o, y_o, dx in zip(x_points, y_points, deriv):
            g = lambda x: dx*(x-x_o)+y_o
            point = axes.coords_to_point(x_o, y_o)
            vertline = axes.get_vertical_line(point, line_config={"dashed_ratio": 0.85}, color =GRAY_D)

            self.play(Create(vertline), run_time = 1)
            self.wait()
            point = axes.coords_to_point(x_o, y_o)
            dot1 = Dot(point, color = '#ff0000', radius = 0.05)
            self.play(Create(dot1), run_time = 1)
            
            self.wait()
            line = axes.plot(g, x_range = [-axtick_ref*2, axtick_ref*2, (2*2*axtick_ref)/2], use_smoothing=True, color = LIGHT_GRAY)
            self.play(Create(line), run_time = 1)
            self.wait()
            fade = FadeOut(vertline)
            fadeline = FadeOut(line)
            fadept = FadeOut(dot1)
            self.play(fade)
            self.wait()
            self.play(fadeline)
            self.wait()
            self.play(fadept)
            self.wait()

def func(x):
    return x**3+x**2

if __name__=="__main__":
    #pass
    integ = Newton_R(func, 10, 0.00, 4.0)
    integ.render()

