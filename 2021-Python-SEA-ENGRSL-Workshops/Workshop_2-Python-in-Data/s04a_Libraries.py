from manim import *

class s04a_Libraries(Scene):

	def construct(self):

		# Actors.

		mainTitle = Text("Libraries")
		subtitleA = Text("Collections of code that can be used in your projects.")

		header = Text("Full basic syntax:")
		code = Code(
			file_name="./code/s04a_s0.py",
			tab_width=4,
			font="Monospace",
			background="window",
			style="monokai",
			language="python",
		)

		texts = [Text(line) for line in (
			"Some libraries are included in a standard",
			"installation of Python. See:",
			"https://docs.python.org/3/library/index.html",
			"Non-standard libraries can be browsed and",
			"installed from https://pypi.org/",
			)
		]

		# Scaling.

		subtitleA.scale(0.75)

		for text in texts:
			text.scale(0.40)

		header.scale(0.66)

		# Positioning.

		mainTitle.to_edge(UP)
		subtitleA.next_to(mainTitle, DOWN).shift(0.25*DOWN)

		code.next_to(subtitleA, DOWN).shift(1*DOWN).to_edge(LEFT)
		header.next_to(code, UP).align_to(code, LEFT)

		texts[0].next_to(code, RIGHT).align_to(code, UP)

		for i in range(1, len(texts)):
			texts[i].next_to(texts[i-1], DOWN).align_to(texts[i-1], LEFT)

		# Animations.

		actors = []

		actors.append(mainTitle)
		self.play(Write(mainTitle))
		self.wait(1)

		actors.append(subtitleA)
		self.play(Write(subtitleA))
		self.wait(1)

		actors.append(header)
		self.play(Write(header))
		actors.append(code)
		self.play(Write(code))
		self.wait(1)

		for text in texts:
			actors.append(text)
			self.play(Write(text))

		# Cleanup.

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in actors])

