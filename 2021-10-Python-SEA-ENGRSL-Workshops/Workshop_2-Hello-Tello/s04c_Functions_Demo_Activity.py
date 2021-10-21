from manim import *

class s04c_Functions_Demo_Activity(Scene):

	def construct(self):

		# Actors.
		title     = Text("Functions")
		subtitles = [
			Text(x).scale(0.75) for x in (
				"(Demo)",
				"(Activity)",
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
			self.wait(0.5)

		for i in range(1, len(subtitles)):
			self.play(Transform(subtitles[0], subtitles[i]))
			self.wait(0.5)

		# Cleanup.
		self.wait(0.5)
		self.play(*[FadeOut(actor) for actor in actors])

