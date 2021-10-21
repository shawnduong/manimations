from manim import *

class s05a_Intro_to_Tello_Drones(Scene):

	def construct(self):

		# Actors.
		title = Text("Intro to Tello Drones")
		points = VGroup(*[
			Text(x) for x in (
				"Tello drones spawn a wireless network.",
				"Users connect to the network and communicate via\n"
					+ "\tthe drone's IP and designated UDP port.",
				"The Python Tello API streamlines and abstracts\n"
					+ "\tthe networking process.",
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

		for actor in actors:
			self.play(Write(actor))

		for point in points:
			self.play(ApplyMethod(point.set_opacity, 1.00))
			self.wait(0.5)
			self.play(ApplyMethod(point.set_opacity, 0.50))

		# Cleanup.
		self.wait(0.5)
		self.play(*[FadeOut(actor) for actor in actors])

