from manim import *

class s05a_Demo_matplotlib(Scene):

	def construct(self):

		# Actors.

		mainTitle = Text("Demo: matplotlib")
		subtitleA = Text("matplotlib is a popular library for data visualization.")

		texts = [
			Text("- Info: https://matplotlib.org/"),
			Text("- Docs: https://matplotlib.org/stable/contents.html"),
		]

		prompt = [
			Text("Suppose that we wanted to create a pie graph of "),
			Text("UC Merced students categorized by their school."),
			Text("matplotlib can do this! Let's look at the code."),
		]

		# Scaling.

		subtitleA.scale(0.75)

		for text in texts:
			text.scale(0.75)

		for text in prompt:
			text.scale(0.66)

		# Positioning.

		mainTitle.to_edge(UP)
		subtitleA.next_to(mainTitle, DOWN).shift(0.25*DOWN)

		texts[0].next_to(subtitleA, DOWN).align_to(subtitleA, LEFT)
		texts[1].next_to(texts[0], DOWN).align_to(texts[0], LEFT)

		prompt[0].next_to(texts[1], DOWN).shift(0.50*DOWN)

		for i in range(1, len(prompt)):
			prompt[i].next_to(prompt[i-1], DOWN).align_to(prompt[i-1], LEFT)

		# Animations.

		actors = []

		actors.append(mainTitle)
		self.play(Write(mainTitle))
		self.wait(1)

		actors.append(subtitleA)
		self.play(Write(subtitleA))
		self.wait(1)

		for text in texts:
			actors.append(text)
			self.play(Write(text))

		self.wait(1)

		for text in prompt:
			actors.append(text)
			self.play(Write(text))

		self.wait(1)

		# Cleanup.

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in actors])

