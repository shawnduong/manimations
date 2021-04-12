from manim import *

class s02a_Title(Scene):

	def construct(self):

		# Actors and scaling.

		mainTitle = Text("Overview of Workshop Activity")
		subtitleA = Text("https://github.com/shawnduong/2021-UCM-ESL-Python-Workshop/").scale(0.50)

		# Positioning.

		mainTitle.shift(0.25*UP)
		subtitleA.next_to(mainTitle, DOWN)

		# Animations.

		actors = [mainTitle, subtitleA]

		for actor in actors:
			self.play(Write(actor))
			self.wait(1)

		# Cleanup.

		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

