from manim import *

class Turing(Scene):

	def construct(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{mathrsfs}\usepackage{amssymb}")

		sqr = Square(side_length = 2.0)

		q1 = Circle(radius = 0.25, color=RED)
		q2 = Circle(radius = 0.25, color=RED)
		q3 = Circle(radius = 0.25, color=RED)
		q4 = Circle(radius = 0.25, color=RED)
		#q1.set_fill(PINK, opacity=0.5)
		g1 = VGroup()
		vt1 = MathTex(r"q_{1}", font_size=24)
		g1.add(q1, vt1)
		vt1.move_to([-3.55,0,1])
		q1.move_to([-3.55,0,1])

		g2 = VGroup()
		vt2 = MathTex(r"q_{2}", font_size=24)
		g2.add(q2, vt2)
		#p1.move_to(q1.point_at_angle(90*DEGREES))
		vt2.move_to([-3.55,-2,1])
		q2.move_to([-3.55,-2,1])

		g3 = VGroup()
		vt3 = MathTex(r"q_{3}", font_size=24)
		g3.add(q3, vt3)
		vt3.move_to([0.0,2.0,1])
		q3.move_to([0.0,2.0,1])

		g4 = VGroup()
		vt4 = MathTex(r"q_{4}", font_size=24)
		g4.add(q4, vt4)
		vt4.move_to([3.55,0,1])
		q4.move_to([3.55,0,1])

		raio_menor = 0.15
		a11 = Arc(radius = raio_menor, start_angle = -90*DEGREES, angle = 300*DEGREES, tip_style={'stroke_width': 0.5},
			tip_length =0.1,
			arc_center=[0.0,2.0+0.25+1*raio_menor,1], stroke_width=1).add_tip()
		t11 = MathTex(r"c: c, R\\b: b, R\\a: a, R", font_size=16)
		t11.move_to((a11.get_end()+a11.get_start())/2 + [0.75, 0.25, 1])

		a22 = Arc(radius = raio_menor, start_angle = -90*DEGREES, angle = 360*DEGREES, tip_style={'stroke_width': 0.5},
			tip_length =0.1,
			arc_center=[3.55,0+0.25+1*raio_menor,1], stroke_width=1).add_tip()
		t22 = MathTex(r"c: c, L\\b: b, L\\a: a, L", font_size=16)
		t22.move_to((a22.get_end()+a22.get_start())/2 + [0.75, 0.25, 1])

		a12 = Arrow(start=[-3.55,0,1], end=[-3.55,-2,1], tip_style={'stroke_width': 0.5}, tip_length =0.1, stroke_width=1)
		t12 = MathTex(r"c: c, R", font_size=16)
		t12.move_to((a12.get_end()+a12.get_start())/2)
		a13 = Arrow(start=[-3.55,0,1], end=[0,2,1], tip_style={'stroke_width': 0.5}, tip_length =0.1, stroke_width=1)
		t13 = MathTex(r"b: \&, R \\a: @, R", font_size=16)
		t13.move_to((a13.get_end()+a13.get_start())/2)
		a34 = Arrow(start=[0,2,1], end=[3.55,0,1], tip_style={'stroke_width': 0.5}, tip_length =0.1, stroke_width=1)
		t34 = Tex(r"$\square: c, L$}", font_size=16, tex_template=myTemplate)
		t34.move_to((a34.get_end()+a34.get_start())/2)
		a41 = Arrow(start=[3.55,0,1], end=[-3.55,0,1], tip_style={'stroke_width': 0.5}, tip_length =0.1, stroke_width=1)
		t41 = MathTex(r"\&: b, R \\@: a, R", font_size=16)
		t41.move_to((a41.get_end()+a41.get_start())/2)
		
		#vertices = [0, 1, 2, 3]
		#edges = [(0, 1), (0, 3), (1, 2), (2, 0)]
		for q in [g1,g2,g3,g4]:
			self.play(Create(q))
		#self.play(Create(g1))
		self.play(Create(a11), Create(a22), Create(a12), Create(a13), Create(a34), Create(a41))
		self.play(Create(t12), Create(t13), Create(t34), Create(t41), Create(t22), Create(t11))
		
		self.wait()

if __name__=="__main__":
	t = Turing()
	t.render()