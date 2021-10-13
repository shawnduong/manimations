from manim import *

class s04a_Why_Py(Scene):

	def construct(self):

		# Actors.
		title = Text("Why Py?")
		points = VGroup(*[
			Text(x) for x in (
				"- Simple and intuitive for non-programmers.",
				"- Low learning curve.",
				"- Interpreted.",
				"- Like a piano!",
			)
		]).scale(0.75)
		footnote = Text("* We will use Python 3 (specifically, 3.7+).").scale(0.75)

		# Positioning.
		title.to_edge(UP+LEFT)
		points.arrange(direction=DOWN, aligned_edge=LEFT)
		points.next_to(title, DOWN).to_edge(LEFT)
		footnote.to_edge(DOWN+LEFT)

		# Opacity.
		points.set_opacity(0.50)

		# Modifiers.
		ul = Underline(title)

		# Animations.

		actors = [title, ul, points, footnote]

		for i in range(len(actors)-1):
			self.play(Write(actors[i]))

		for point in points:
			self.play(ApplyMethod(point.set_opacity, 1.00))
			self.wait(1)
			self.play(ApplyMethod(point.set_opacity, 0.50))

		self.play(Write(footnote))

		# Cleanup.
		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

