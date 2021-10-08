from manim import *

class s00a_Title(Scene):

	def construct(self):

		# Actors and scaling.

		mainTitle = Text("Python in Security")
		subtitleA = Text("Creating Cybersecurity Tools Using Python").scale(0.75)

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

