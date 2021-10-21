from manim import *

class s07a_Basic_Tello_Methods(Scene):

	def construct(self):

		# Actors.
		title = Text("Basic Tello Methods")
		code = Code(
			file_name="./code/s07a_s0.py",
			tab_width=4,
			font="Monospace",
			background="window",
			style="monokai",
			language="python",
		).scale(0.40)

		# Positioning
		title.to_edge(UP)

		# Modifiers.
		ul = Underline(title)

		# Animations.

		actors = [title, ul, code]

		for i in range(len(actors)):

			self.play(Write(actors[i]))

			if i > 1:
				self.wait(0.5)

		# Cleanup.
		self.wait(0.5)
		self.play(*[FadeOut(actor) for actor in actors])

