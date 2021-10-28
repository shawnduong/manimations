from manim import *

class s02a_Basic_Programming_Concepts_Review(Scene):

	def construct(self):

		# Actors.
		title = Text("Basic Programming Concepts Review")
		points = VGroup(*[
			Text(x) for x in (
				"- Conditionals",
				"- While Loops",
				"- For x in y Loops",
				"- For x in range(y) Loops",
				"- Functions",
			)
		]).scale(0.75)

		# Positioning.
		title.to_edge(UP+LEFT)
		points.arrange(direction=DOWN, aligned_edge=LEFT)
		points.next_to(title, DOWN).to_edge(LEFT)

		# Opacity.
		points.set_opacity(0.50)

		# Modifiers.
		ul = Underline(title)

		# Animations.

		actors = [title, ul, *points]

		for actor in actors:
			self.play(Write(actor))

		for point in points:
			self.play(ApplyMethod(point.set_opacity, 1.00))
			self.wait(0.5)
			self.play(ApplyMethod(point.set_opacity, 0.50))

		# Cleanup.
		self.wait(0.5)
		self.play(*[FadeOut(actor) for actor in actors])

