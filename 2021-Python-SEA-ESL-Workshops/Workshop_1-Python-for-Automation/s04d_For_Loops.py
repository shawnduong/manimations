from manim import *

class s04d_For_Loops(Scene):

	def construct(self):

		mainTitle = Text("There's another kind of loop: for loops.")
		subtitleA = Text("These are derived from while loops and").scale(0.75)
		subtitleB = Text("will be taught next week.").scale(0.75)

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

