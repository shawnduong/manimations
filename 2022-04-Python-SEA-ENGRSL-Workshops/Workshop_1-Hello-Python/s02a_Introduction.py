from manim import *

class s02a_Introduction(Scene):

	def construct(self):

		# Actors.
		title = Text("Introduction")
		points = VGroup(*[
			Text(x) for x in (
				"Goal: Learn programming with Python, fly\n" + 
					"\tsome awesome drones, and have fun!",
				"Day 1 - Hello Python!",
				"Day 2 - Hello Tello!",
				"Day 3 - Go Go Tello!",
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

		actors = [title, ul, points]

		for i in range(len(actors)):
			self.play(Write(actors[i]))

		for point in points:
			self.play(ApplyMethod(point.set_opacity, 1.00))
			self.wait(1)
			self.play(ApplyMethod(point.set_opacity, 0.50))

		# Cleanup.
		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

