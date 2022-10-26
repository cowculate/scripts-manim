from manim import *

class Inercia(Scene):
	def construct(self):

		line = Line([-7-1/9, -1, 0], [7+1/9, -1, 0])
		self.add(line)

		circ = Circle(radius = 1, color=RED, fill_opacity=1)

		normal_force_vector = Arrow([0, 1, 0], [0, 2, 0], buff=0, color=BLUE_E)
		weight_force_vector = Arrow([0, -1, 0], [0, -2, 0], buff=0, color=TEAL_E)
		external_force_vector = Arrow([1,0, 0], [2, 0, 0], buff=0, color=GOLD)


		null_resultant = Text("Resultante nula").to_edge(UP)
		right_resultant = Text("Resultante para a direita").to_edge(UP)

		group = VGroup(circ, normal_force_vector, weight_force_vector, external_force_vector)

		self.play(GrowFromCenter(circ))
		self.play(GrowArrow(normal_force_vector), GrowArrow(weight_force_vector), FadeIn(null_resultant))

		self.wait(2)

		self.play(FadeOut(null_resultant))
		self.play(GrowArrow(external_force_vector), FadeIn(right_resultant))
		self.wait(1)
		self.play(group.animate.move_to([10, 0, 0]))

		group.move_to([-10, 0, 0])

		self.play(group.animate.move_to([0.5, 0, 0]))

		self.play(FadeOut(right_resultant))
		self.play(FadeOut(group))
		self.wait(1)