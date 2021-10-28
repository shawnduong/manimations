from manim import *

class s00a_Title(Scene):

	def construct(self):

		# Actors.
		title     = Text("Go Go Tello!")
		subtitle  = Text("Week 3/3").scale(0.75)
		footnote  = VGroup(*[
			Text(x).scale(0.50) for x in (
				"Made possible by the Solar Energy Association",
				"and Engineering Service Learning at UC Merced.",
			)
		])

		# Positioning.
		title.shift(0.50*UP)
		subtitle.next_to(title, DOWN)
		footnote[0].next_to(subtitle, DOWN).shift(0.5*DOWN)
		footnote[1].next_to(footnote[0], DOWN)

		# Animations.

		actors = [title, subtitle, footnote]

		for actor in actors:
			self.play(Write(actor))
			self.wait(0.5)

		# Cleanup.
		self.wait(0.5)
		self.play(*[FadeOut(actor) for actor in actors])

