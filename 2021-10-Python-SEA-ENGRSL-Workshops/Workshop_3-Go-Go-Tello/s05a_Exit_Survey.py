from manim import *

class s05a_Exit_Survey(Scene):

	def construct(self):

		# Actors.
		title = Text("Exit Survey")
		qr = ImageMobject("./img/survey_qr.png")

		# Positioning.
		title.to_edge(UP)
		qr.shift(0.5*DOWN)

		# Modifiers.
		ul = Underline(title)

		# Animations.

		actors = [title, ul, qr]

		self.play(Write(actors[0]))
		self.play(Write(actors[1]))
		self.wait(0.5)
		self.play(FadeIn(actors[2]))

		# Cleanup.
		self.wait(0.5)
		self.play(*[FadeOut(actor) for actor in actors])

