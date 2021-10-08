from manim import *

class s02b_Differences(Scene):

	def construct(self):

		# Actors and scaling.

		subtitleA = Text("While loops are condition based,").scale(0.75)
		subtitleB = Text("and for loops are iteration based.").scale(0.75)

		# Positioning.

		subtitleA.shift(0.25*UP)
		subtitleB.next_to(subtitleA, DOWN)

		# Animations.

		actors = [subtitleA, subtitleB]

		self.play(Write(subtitleA))
		self.play(Write(subtitleB))

		# Cleanup.

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in actors])

