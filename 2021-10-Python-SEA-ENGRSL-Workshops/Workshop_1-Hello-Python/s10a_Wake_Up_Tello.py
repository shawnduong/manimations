from manim import *

class s10a_Wake_Up_Tello(Scene):

	def construct(self):

		# Actors.
		text = Text("Let's wake up Tello!").scale(0.75)
		pointsA = VGroup(*[
			Text(x) for x in (
				"The drone",
				"- has a front camera.",
				"- spawns a wireless network.",
				"- broadcasts an SSID.",
			)
		]).scale(0.75)
		pointsB = VGroup(*[
			Text(x) for x in (
				"The API",
				"- abstracts.",
				"- utilizes OOP.",
				"- makes life easier.",
			)
		]).scale(0.75)

		# Positioning.
		text.to_edge(UP+LEFT)
		pointsA.arrange(direction=DOWN, aligned_edge=LEFT)
		pointsA.next_to(text, DOWN).to_edge(LEFT).shift(0.1*DOWN)
		pointsB.arrange(direction=DOWN, aligned_edge=LEFT)
		pointsB.next_to(pointsA, DOWN).to_edge(LEFT).shift(0.1*DOWN)

		# Opacity.
		pointsA.set_opacity(0.50)
		pointsB.set_opacity(0.50)

		# Animations.

		actors = [text, pointsA, pointsB]

		self.play(Write(text))
		self.wait(1)

		self.play(Write(pointsA))
		self.play(Write(pointsB))
		self.wait(1)

		self.play(ApplyMethod(pointsA.set_opacity, 1.00))
		self.wait(1)
		self.play(ApplyMethod(pointsA.set_opacity, 0.50))

		self.play(ApplyMethod(pointsB.set_opacity, 1.00))
		self.wait(1)
		self.play(ApplyMethod(pointsB.set_opacity, 0.50))

		# Cleanup.
		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

