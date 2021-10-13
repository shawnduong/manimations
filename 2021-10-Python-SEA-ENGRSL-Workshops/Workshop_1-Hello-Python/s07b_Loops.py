from manim import *

class s07b_Loops(Scene):

	def construct(self):

		# Actors.
		title = Text("Loops")
		points = VGroup(*[
			Text(x).scale(0.75) for x in (
				"While ________, do ________.",
				"For ________ in ________, do ________.",
				"For ________ many times, do ________.",
			)
		])
		code = [
			Code(
				file_name="./code/s07b_s0.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			),
			Code(
				file_name="./code/s07b_s1.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			),
			Code(
				file_name="./code/s07b_s2.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			),
		]

		# Positioning.

		title.to_edge(UP+LEFT)
		points.arrange(direction=DOWN, aligned_edge=LEFT)
		points.next_to(title, DOWN).to_edge(LEFT)
		code[0].shift(1.5*DOWN)

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

		actors.append(points[1])
		self.play(Write(points[1]))
		self.wait(1)

		self.play(Write(code[1]))
		self.remove(code[0])
		self.wait(1)

		actors.append(points[2])
		self.play(Write(points[2]))
		self.wait(1)

		actors.append(code[2])
		self.play(Write(code[2]), FadeOut(code[1]))
		self.wait(1)

		# Cleanup.
		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

