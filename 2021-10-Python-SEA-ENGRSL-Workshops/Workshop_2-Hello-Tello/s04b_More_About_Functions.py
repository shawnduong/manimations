from manim import *

class s04b_More_About_Functions(Scene):

	def construct(self):

		# Actors.
		title = Text("More About Functions")
		point = Text("To create a function, we just define it.").scale(0.75)
		code = [
			Code(
				file_name="./code/s04b_s0.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			),
			Code(
				file_name="./code/s04b_s1.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			),
			Code(
				file_name="./code/s04b_s2.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			),
		]
		remarks = [
			Text("Functions can have inputs, called parameters.").scale(0.50),
			Text("Functions can also return values.").scale(0.50),
			Text("Each function has its own local context, called a scope.").scale(0.50),
		]

		# Positioning
		title.to_edge(UP+LEFT)
		point.next_to(title, DOWN).to_edge(LEFT)
		code[0].shift(0.5*UP)
		code[1].shift(0.5*UP)
		code[2].shift(0.5*UP)
		remarks[0].to_edge(DOWN).shift(2*UP)
		remarks[1].next_to(remarks[0], DOWN)
		remarks[2].next_to(remarks[1], DOWN)

		# Modifiers.
		ul = Underline(title)

		# Highlights.
		highlights = [
			SurroundingRectangle(point[24:27], fill_color="#FFFF00",
				fill_opacity=0.25, stroke_width=0, buff=0.05),
			SurroundingRectangle(remarks[2], fill_color="#FFFF00",
				fill_opacity=0.25, stroke_width=0, buff=0.05),
		]

		# Animations.

		self.add(title)
		self.add(ul)

		actors = [title, ul, point, highlights[0], code[0], remarks[0], code[1], remarks[1], code[2], remarks[2], highlights[1]]

		for i in range(2, len(actors)):

			self.play(Write(actors[i]))
			self.wait(0.5)

		# Cleanup.
		self.remove(code[0])
		self.remove(code[1])
		actors.remove(code[0])
		actors.remove(code[1])
		self.wait(0.5)
		self.play(*[FadeOut(actor) for actor in actors])

