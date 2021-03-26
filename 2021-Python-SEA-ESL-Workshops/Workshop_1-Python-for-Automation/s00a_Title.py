from manim import *

class s00a_Title(Scene):

	def construct(self):

		mainTitle = Text("Python for Automation")
		subtitleA = Text("Making Your Job Easier Using Python")

		subtitleA.scale(0.75)

		mainTitle.shift(0.25*UP)
		subtitleA.next_to(mainTitle, DOWN)

		actors = [mainTitle, subtitleA]

		for actor in actors:
			self.play(Write(actor))
			self.wait(1)

		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

