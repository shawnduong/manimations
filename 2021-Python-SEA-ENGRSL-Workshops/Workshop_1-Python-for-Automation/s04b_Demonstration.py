from manim import *

class s04b_Demonstration(Scene):

	def construct(self):

		mainTitle = Text("Demonstration")

		self.play(Write(mainTitle))

		self.wait(3)
		self.play(FadeOut(mainTitle))

