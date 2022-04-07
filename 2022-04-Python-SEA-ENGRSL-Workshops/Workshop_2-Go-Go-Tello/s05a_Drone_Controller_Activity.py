from manim import *

class s05a_Drone_Controller_Activity(Scene):

	def construct(self):

		# Actors.
		title     = Text("Drone Controller")
		subtitle  = Text("(Activity)").scale(0.75)

		# Positioning.
		title.shift(0.50*UP)
		subtitle.next_to(title, DOWN)

		# Animations.

		actors = [title, subtitle]

		for actor in actors:
			self.play(Write(actor))
			self.wait(1)

		# Cleanup.
		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

