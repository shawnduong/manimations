from manim import *

class s08a_Functions(Scene):

	def construct(self):

		# Actors.
		title = Text("Functions")
		point = Text("What if there are chunks of code that we\n" +
			"have to use in multiple places?").scale(0.75)
		code = [
			Code(
				file_name="./code/s08a_s0.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			).scale(0.30),
			Code(
				file_name="./code/s08a_s1.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			).scale(0.30),
		]
		remarks = [
			Text("We can define\nit as a function!").scale(0.50),
			Text("We'll talk more about this in-depth next week!").scale(0.50),
			Text("* Pedantic note *").scale(0.50),
		]

		# Positioning
		title.to_edge(UP+LEFT)
		point.next_to(title, DOWN).to_edge(LEFT)
		code[0].next_to(point, DOWN)
		remarks[0].shift(1*LEFT)
		remarks[0].set_z_index(-1)
		remarks[1].to_edge(DOWN).shift(1*UP)
		remarks[2].to_edge(DOWN)

		# Modifiers.
		ul = Underline(title)

		# Animations.

		actors = [title, ul, point]

		for i in range(len(actors)):

			self.play(Write(actors[i]))

			if i > 1:
				self.wait(1)

		self.play(Write(code[0]))
		self.wait(1)

		actors.append(remarks[0])
		self.add(remarks[0])
		self.play(ApplyMethod(code[0].shift, 2*LEFT), ApplyMethod(remarks[0].shift, 2*RIGHT))
		self.wait(1)

		code[1].move_to(code[0], UP+LEFT)
		actors.append(code[1])
		self.play(Write(code[1]))
		self.remove(code[0])
		self.wait(1)

		actors.append(remarks[1])
		self.play(Write(remarks[1]))
		self.wait(1)

		actors.append(remarks[2])
		self.play(Write(remarks[2]))
		self.wait(1)

		# Cleanup.
		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

