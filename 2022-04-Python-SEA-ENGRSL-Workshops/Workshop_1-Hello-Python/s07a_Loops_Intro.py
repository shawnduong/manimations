from manim import *

class s07a_Loops_Intro(Scene):

	def construct(self):

		# Actors.
		text = Text("What if we want to do something\nN many times?").scale(0.75)
		code = [
			Code(
				file_name="./code/s07a_s0.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			),
			Code(
				file_name="./code/s07a_s1.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			),
			Code(
				file_name="./code/s07a_s2.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			),
			Code(
				file_name="./code/s07a_s3.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			),
		]
		remark = Text("There has to\nbe an easier\nway to do this!").scale(0.75)

		# Positioning.

		text.to_edge(UP+LEFT)
		code[0].shift(2*LEFT + 1*UP)

		for i in range(1, len(code)):
			code[i].move_to(code[0], UP+LEFT)

		remark.next_to(code[0], RIGHT).shift(0.25*RIGHT)

		# Animations.

		actors = [text, code[-1]]

		self.play(Write(text))
		self.wait(1)

		self.play(Write(code[0]))
		self.wait(1)

		for i in range(1, len(code)):
			self.play(Write(code[i]))
			self.remove(code[i-1])
			self.wait(1)

		actors.append(remark)
		self.play(Write(remark))
		self.wait(1)

		# Cleanup.
		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

