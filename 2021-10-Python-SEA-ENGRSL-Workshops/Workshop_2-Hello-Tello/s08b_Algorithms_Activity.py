from manim import *

class s08b_Algorithms_Activity(Scene):

	def construct(self):

		# Actors.
		title     = Text("Algorithms")
		subtitle  = Text("(Activity)").scale(0.75)

		# Positioning.
		title.shift(0.50*UP)
		subtitle.next_to(title, DOWN)

		# Animations.

		actors = [title, subtitle]

		for actor in actors:
			self.play(Write(actor))
			self.wait(0.5)

		# Cleanup.
		self.wait(0.5)
		self.play(*[FadeOut(actor) for actor in actors])

