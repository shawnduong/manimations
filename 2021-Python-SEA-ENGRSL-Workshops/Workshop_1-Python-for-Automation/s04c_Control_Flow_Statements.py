from manim import *

class s04c_Control_Flow_Statements(Scene):

	def construct(self):

		mainTitle = Text("Control Flow Statements")
		subtitleA = Text("Consider the following instructions.")
		subtitleB = Text("This is a looping program.")
		subtitleC = Text("Consider the following program.")
		subtitles = [
			subtitleA, subtitleB, subtitleC
		]

		loopingProgram = [Text(line) for line in (
			"1. While it is daytime, continue. Else, stop.",
			"2. Go to step 3 if there are no people home. Else, 4.",
			"3. Ensure that the lights are off.",
			"4. Wait a minute before checking again. Go to step 1.",
			)
		]

		codeA = Code(
			file_name="./code/s04c_s0.py",
			tab_width=4,
			font="Monospace",
			background="window",
			style="monokai",
			language="python",
		)

		lightbulb = {
			"dim": ImageMobject("./img/lightbulb_dim.png"),
			"lit": ImageMobject("./img/lightbulb_lit.png"),
		}

		assumptions = [
			Text("Assume that it is daytime and someone is home."),
			Text("Someone left the house, and now nobody is home."),
			Text("Someone just came home and turned the lights on."),
			Text("It is no longer daytime."),
		]

		for subtitle in [*subtitles, *assumptions]:
			subtitle.scale(0.66)

		for line in loopingProgram:
			line.scale(0.50)

		mainTitle.to_edge(UP)

		for subtitle in subtitles:
			subtitle.next_to(mainTitle, DOWN).shift(0.25*DOWN)

		for assumption in assumptions:
			assumption.next_to(subtitleA, DOWN)

		subtitleB.next_to(subtitleA, DOWN)
		subtitleC.move_to(subtitleA, DOWN)

		loopingProgram[0].next_to(subtitleB, DOWN).shift(0.25*DOWN + 2*LEFT)

		for i in range(1, len(loopingProgram)):
			loopingProgram[i].next_to(loopingProgram[i-1], DOWN).align_to(loopingProgram[i-1], LEFT)

		codeA.next_to(loopingProgram[-1], DOWN).align_to(loopingProgram[-1], LEFT)

		lightbulb["dim"].next_to(codeA, RIGHT).shift(1*RIGHT)
		lightbulb["lit"].move_to(lightbulb["dim"])

		actors = [mainTitle, subtitleA]

		for actor in actors:
			self.wait(1)
			self.play(Write(actor))

		for line in loopingProgram:
			actors.append(line)
			self.wait(1)
			self.play(Write(line))

		self.wait(1)
		actors.append(subtitleB)
		self.play(Write(subtitleB))

		self.wait(1)
		actors.remove(subtitleA)
		actors.remove(subtitleB)
		self.play(*[FadeOut(actor) for actor in (subtitleA, subtitleB)])

		self.wait(1)
		actors.append(subtitleC)
		actors.append(codeA)
		self.play(Write(subtitleC), Write(codeA))
		actors.append(assumptions[-1])  # Final state
		actors.append(lightbulb["lit"]) # Final state
		self.play(Write(assumptions[0]))
		self.play(FadeIn(lightbulb["lit"]))

		# This next series of animations took the complete combined effort of my last 3 remaining brain cells.

		# Index     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
		sequence = (1, 3, 0, 1, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 3, 0)
		mappings = {
			 5: 1,
			13: 2,
			16: 3,
		}

		highlightsA = [SurroundingRectangle(line, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0, buff=0.05) for line in (
			# Dumb fix for tabs.
			codeA[2][0], codeA[2][1][1:], codeA[2][2][2:], codeA[2][3][1:]
			)
		]
		highlighter = highlightsA[0].copy()

		self.wait(1)
		self.play(Write(highlighter))

		a = 0

		for i in range(len(sequence)):

			self.wait(1)

			if i in mappings.keys():
				self.play(FadeOut(assumptions[a]))
				a = mappings[i]
				self.play(Write(assumptions[a]))

			if i == 8:
				self.play(FadeOut(lightbulb["lit"]), FadeIn(lightbulb["dim"]))

			elif i == 13:
				self.play(FadeOut(lightbulb["dim"]), FadeIn(lightbulb["lit"]))

			self.play(Transform(highlighter, highlightsA[sequence[i]]))

		self.wait(1)
		self.play(FadeOut(highlighter))

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in actors])

