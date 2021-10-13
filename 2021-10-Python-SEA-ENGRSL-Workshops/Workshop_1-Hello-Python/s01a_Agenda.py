from manim import *

class s01a_Agenda(Scene):

	def construct(self):

		# Actors.
		title = Text("Agenda")
		points = VGroup(*[
			Text(x) for x in (
				"- Intro to the Series",
				"- The Big Picture Idea",
				"- Why Py?",
				"- Logic",
				"- Conditionals",
				"- Loops",
				"- Functions",
			)
		]).scale(0.75)

		# Positioning.
		title.to_edge(UP+LEFT)
		points.arrange(direction=DOWN, aligned_edge=LEFT)
		points.next_to(title, DOWN).to_edge(LEFT)

		# Modifiers.
		ul = Underline(title)

		# Animations.

		actors = [title, ul, *points]

		for i in range(len(actors)):

			self.play(Write(actors[i]))

			if i > 1:
				self.wait(1)

		# Cleanup.
		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

