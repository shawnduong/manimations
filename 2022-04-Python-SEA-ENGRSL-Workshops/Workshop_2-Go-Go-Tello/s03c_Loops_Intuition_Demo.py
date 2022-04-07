from manim import *

class s03c_Loops_Intuition_Demo(Scene):

	def construct(self):

		# Actors.
		title     = Text("Loops")
		subtitles = [
			Text(x).scale(0.75) for x in (
				"(Intuition)",
				"(Demo)",
			)
		]

		# Positioning.

		title.shift(0.50*UP)

		for subtitle in subtitles:
			subtitle.next_to(title, DOWN)

		# Animations.

		actors = [title, subtitles[0]]

		for actor in actors:
			self.play(Write(actor))
			self.wait(1)

		for i in range(1, len(subtitles)):
			self.play(Transform(subtitles[0], subtitles[i]))
			self.wait(1)

		# Cleanup.
		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

