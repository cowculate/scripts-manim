from manim import *

class BubbleSort(Scene):
	def construct(self):

		arr = list()
		num_arr = [5, 1, 4, 2, 8, 9, 3]


		for i in range(7):

			sqr = Square(1)
			num = Text(str(num_arr[i]))

			cell = Group(sqr, num)

			arr.append(cell)
			arr[i].move_to([i-3, 0, 0])


		self.wait(1)
		self.play(FadeIn(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6]))

		#

		for i in range(len(num_arr) - 1):

			for j in range(0, len(num_arr)-i-1):

				self.play(
					arr[j].animate.move_to([arr[j].get_x(), 0.2, 0]),
			  		arr[j+1].animate.move_to([arr[j+1].get_x(), 0.2, 0])
				  )

				if num_arr[j] > num_arr[j + 1]:

					self.bring_to_front(arr[j]) 
					self.bring_to_front(arr[j+1]) 

					self.play(
						arr[j].animate.set_color(RED),
			  			arr[j+1].animate.set_color(RED)
			  			)

					num_arr[j], num_arr[j + 1] = num_arr[j + 1], num_arr[j]

					self.play(Swap(arr[j], arr[j+1]))
					arr[j], arr[j+1] = arr[j+1], arr[j]

					self.play(
						arr[j].animate.set_color(WHITE),
			  			arr[j+1].animate.set_color(WHITE)
			  			)

				self.play(
					arr[j].animate.move_to([arr[j].get_x(), 0, 0]),
				  	arr[j+1].animate.move_to([arr[j+1].get_x(), 0, 0])
				  )

		self.wait(1)
		self.play(FadeOut(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6]))
