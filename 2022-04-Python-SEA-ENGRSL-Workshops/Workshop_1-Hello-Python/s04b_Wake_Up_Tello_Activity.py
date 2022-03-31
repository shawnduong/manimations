from manim import *

class s04b_Wake_Up_Tello_Activity(Scene):

	def construct(self):

		# Actors.
		title     = Text("Wake up, Tello!")
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

