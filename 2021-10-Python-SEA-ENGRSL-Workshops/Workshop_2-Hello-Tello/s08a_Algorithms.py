from manim import *

class s08a_Algorithms(Scene):

	def construct(self):

		# Actors.
		title = Text("Algorithms")
		definition = ImageMobject("./img/algo_def.png")

		# Positioning.
		title.to_edge(UP)

		# Modifiers.
		ul = Underline(title)

		# Animations.

		actors = [title, ul, definition]

		self.play(Write(actors[0]))
		self.play(Write(actors[1]))
		self.wait(0.5)
		self.play(FadeIn(actors[2]))

		# Cleanup.
		self.wait(0.5)
		self.play(*[FadeOut(actor) for actor in actors])

