from manim import *

class s06a_Activity(Scene):

	def construct(self):

		mainTitle = Text("Activity: Generating a Line Graph")
		subtitleA = Text("Prepare to split into groups").scale(0.75)
		subtitleB = Text("and gain hands-on experience!").scale(0.75)

		mainTitle.shift(0.25*UP)
		subtitleA.next_to(mainTitle, DOWN)
		subtitleB.next_to(subtitleA, DOWN)

		actors = [mainTitle, subtitleA, subtitleB]

		self.play(Write(mainTitle))
		self.wait(1)
		self.play(Write(subtitleA))
		self.play(Write(subtitleB))

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in actors])

