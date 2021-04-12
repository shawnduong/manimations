from manim import *

class s05a_Functions(Scene):

	def construct(self):

		# Actors.

		mainTitle = Text("Review: Functions")
		subtitles = [
			Text("A defined collection of instructions with a singular purpose."), # 0
			Text("Functions allow for a program to be broken into smaller,"),      # 1
			Text("repeatable steps with typically deterministic outputs."),        # 2
		]

		header = Text("Full basic syntax:")
		code = Code(
			file_name="./code/s05a_s0.py",
			tab_width=4,
			font="Monospace",
			background="window",
			style="monokai",
			language="python",
		)
		footnote = Tex("Where there are $n$ many inputs and $m$ many outputs.")

		# Scaling.

		for subtitle in subtitles:
			subtitle.scale(0.66)

		header.scale(0.66)

		# Positioning.

		mainTitle.to_edge(UP)
		
		for subtitle in subtitles:
			subtitle.next_to(mainTitle, DOWN).shift(0.25*DOWN)

		subtitles[2].next_to(subtitles[1], DOWN)

		code.next_to(subtitles[2], DOWN).shift(1*DOWN)
		header.next_to(code, UP).align_to(code, LEFT)
		footnote.next_to(code, DOWN).align_to(code, LEFT)

		# Animations.

		actors = []

		actors.append(mainTitle)
		self.play(Write(mainTitle))
		self.wait(1)

		actors.append(subtitles[0])
		self.play(Write(subtitles[0]))
		self.wait(1)

		actors.append(header)
		self.play(Write(header))
		actors.append(code)
		self.play(Write(code))
		actors.append(footnote)
		self.play(Write(footnote))
		self.wait(1)

		actors.remove(subtitles[0])
		self.play(FadeOut(subtitles[0]))
		actors.append(subtitles[1])
		self.play(Write(subtitles[1]))
		actors.append(subtitles[2])
		self.play(Write(subtitles[2]))
		self.wait(1)

		# Cleanup.

		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

