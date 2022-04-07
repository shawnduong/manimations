import numpy as np
from manim import *

class s02a_Conditionals(Scene):

	def construct(self):

		# Actors.
		title = Text("Conditionals")
		points = [
			Text(x).scale(0.75) for x in (
				"If ________, then ________.",
				"Else if ________, then ________.",
				"Else if ________, then ________.",
				"Else if ________, then ________.",
				"Else if ________, then ________.",
				"Else if ________, then ________.",
				"Else ________.",
			)
		]
		code = [
			Code(
				file_name="./code/s02a_s0.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			),
			Code(
				file_name="./code/s02a_s1.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			),
			Code(
				file_name="./code/s02a_s2.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			),
			Code(
				file_name="./code/s02a_s3.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			),
		]

		# Positioning.

		title.to_edge(UP+LEFT)
		points[0].next_to(title, DOWN).to_edge(LEFT)
		points[-1].next_to(points[0], DOWN).to_edge(LEFT)

		for i in range(1, len(points)-1):
			points[i].next_to(points[0], DOWN).to_edge(LEFT)

		code[0].shift(4*RIGHT + 2*UP)

		for i in range(1, len(code)):
			code[i].move_to(code[0], UP+LEFT)

		# Modifiers.
		ul = Underline(title)

		# Animations.

		actors = [title, ul, points[0]]

		for i in range(len(actors)):

			self.play(Write(actors[i]))

			if i > 1:
				self.wait(1)

		self.play(Write(code[0]))
		self.wait(1)

		actors.append(points[-1])
		self.play(Write(points[-1]))
		self.wait(1)

		self.play(Write(code[1]))
		self.remove(code[0])
		self.wait(1)

		actors.append(points[1])
		self.play(
			ApplyMethod(
				points[-1].next_to, points[1],
				np.array([0., -1., 0.]), 0.25,
				np.array([-1., 0., 0.])
			)
		)
		self.play(Write(points[1]))
		self.wait(1)

		self.play(Write(code[2]))
		self.remove(code[1])
		self.wait(1)

		for i in range(2, len(points)-1):
			actors.append(points[i])

		self.play(ApplyMethod(points[-1].shift, DOWN * (len(points)-3)))
		self.play(*[
			ApplyMethod(points[i].shift, DOWN * (i*0.90 - 1)) for i in range(2, len(points)-1)
		])
		self.wait(1)

		actors.append(code[3])
		self.play(Write(code[3]))
		self.remove(code[2])
		self.wait(1)

		# Cleanup.
		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

