from manim import *
import numpy as np
from sympy import * 

def stopCritterion(p_0: 'float', p_1: 'float', eps: 'float') -> 'bool':
    if abs(p_1 - p_0) >= eps:
        return False
    else: return True


def bissec(p_0, p_1, f, iterations, eps):
    x_points = [(p_0, p_0+(p_1-p_0)/2, p_1)]
    y_points = []
    #f_diff = lambdify(Symbol('x'), f(Symbol('x')).diff(Symbol('x')), 'numpy')

    for i in range(0, iterations):
        y = float(f(p_0+(p_1-p_0)/2))

        #evalu = y
        #dv = f_diff(p_0)


        #deriv.append(dv)
        y_points.append((float(f(p_0)), y, float(f(p_1))))

        #p = p_0 - evalu/dv
        if(y<0):
        	p_0 = p_0+(p_1-p_0)/2
        elif(y>0):
        	p_1 = p_0+(p_1-p_0)/2
        elif(y==0):
        	break

        if stopCritterion(p_0, p_1, eps):
            break

        x_points.append((p_0, p_0+(p_1-p_0)/2, p_1))
    return x_points, y_points

def func(x):
    return x**3

class Bissec(Scene):
	def __init__(self, func, iterations, eps, p_0, p_1):
		super().__init__()
		self.function_2exec = func
		self.iterations = iterations
		self.eps = eps
		self.p_0 = p_0
		self.p_1 = p_1

	def construct(self):
		x_lim = max(self.p_0, -self.p_0, self.p_1, -self.p_1)
		y_lim = max(float(self.function_2exec(self.p_0)), -float(self.function_2exec(self.p_0)), -float(self.function_2exec(self.p_1)), float(self.function_2exec(self.p_0)))
		axtick_ref = min(x_lim, y_lim)
		axes = Axes(x_range = [-x_lim*2, x_lim*2, (2*2*axtick_ref)/2], y_range = [-y_lim*2, y_lim*2, (2*2*axtick_ref)/2],
		axis_config = {"numbers_to_exclude": [0], "include_numbers": False, "stroke_width": 0.5, "include_ticks": False}, tips = False)
        
		axis_labels = axes.get_axis_labels(x_label = "x", y_label = "f(x)")

		graph = axes.plot(self.function_2exec, x_range=[-x_lim*2, x_lim*2], use_smoothing=True)
		self.add(axes, graph)
		graphing_stuff = VGroup(axes, graph, axis_labels)

		x_points, y_points = bissec(self.p_0, self.p_1, self.function_2exec, self.iterations, self.eps)

		self.play(Create(graph), run_time = 2)
		
		self.wait()
		print(x_points)
		for x_o, y_o in zip(x_points, y_points):
			#g = lambda x: dx*(x-x_o)+y_o
			point0 = axes.coords_to_point(x_o[0], y_o[0])
			point1 = axes.coords_to_point(x_o[2], y_o[2])
			#point2 = axes.coords_to_point(x_o[1], y_o[1])
			vertline0 = axes.get_vertical_line(point0, line_config={"dashed_ratio": 0.85}, color =GRAY_D)
			vertline1 = axes.get_vertical_line(point1, line_config={"dashed_ratio": 0.85}, color =GRAY_D)

			self.play(Create(vertline0), Create(vertline1), run_time = 1)
			#self.wait()
			#point0 = axes.coords_to_point(x_o[0], y_o[0])
			#point1 = axes.coords_to_point(x_o[2], y_o[2])
			dot0 = Dot(point0, color = '#ff0000', radius = 0.05)
			dot1 = Dot(point1, color = '#ff0000', radius = 0.05)
			self.play(Create(dot0), Create(dot1), run_time = 1)
            
			#self.wait()

			#dot2 = Dot(point2, color = '#ff0000', radius = 0.05)
			#self.play(Create(dot2), run_time = 1)
			fade = FadeOut(vertline0, vertline1, dot0, dot1)
			#fadeline = FadeOut(line)
			#fadept = FadeOut(dot1)
			self.play(fade)
			#self.play(fadeline)
			#self.play(fadept)
			self.wait()

if __name__=="__main__":
	#func, iterations, eps, p_0, p_1
	integ = Bissec(func, 100, 0.05, -5.0, 1.0)
	integ.render()