from manim import *

class s04a_Control_Flow_Statements(Scene):

	def construct(self):

		mainTitle = Text("Control Flow Statements")
		subtitleA = Text("Consider the following instructions.")
		subtitleB = Text("This is a linear program.")
		subtitleC = Text("This is a non-linear program.")
		subtitleD = Text("Python can handle conditionals and loops.")
		subtitleE = Text("Consider the following program.")
		subtitleF = Text("Assume that lightAreOn is: True")
		subtitleG = Text("Assume that lightAreOn is: False")
		subtitles = [
			subtitleA, subtitleB, subtitleC, subtitleD,
			subtitleE, subtitleF, subtitleG,
		]

		linearProgram = [Text(line) for line in (
			"1. Preheat oven to 175 C.",
			"2. Cream together butter and sugar.",
			"3. Beat in eggs.",
			"4. Stir in vanilla and baking soda.",
			"5. Stir in flour and chocolate chips.",
			"6. Drop by spoonfuls into baking sheet.",
			"7. Bake for 15 minutes.",
			)
		]
		nonlinearProgram = [Text(line) for line in (
			"1. Go to the first battery.",
			"2. If it is powered on, go to step 3. Else, step 4.",
			"3. Record the charge and go to step 5.",
			"4. Turn the battery on and go to step 5.",
			"5. If there is a next battery, repeat steps 2-5 for it.",
			)
		]

		codeA = Code(
			file_name="./code/s04a_s0.py",
			tab_width=4,
			font="Monospace",
			background="window",
			style="monokai",
			language="python",
		)
		outputA = Code(
			file_name="./code/s04a_o0.txt",
			tab_width=4,
			font="Monospace",
			background="window",
			insert_line_no=False,
			style="monokai",
			language="text",
		)
		outputB = Code(
			file_name="./code/s04a_o1.txt",
			tab_width=4,
			font="Monospace",
			background="window",
			insert_line_no=False,
			style="monokai",
			language="text",
		)
		codeAExplained= [Text(line).scale(0.50) for line in (
			"1. If the lights are on, go to step 2. Else, step 3.",
			"2. Print out the string \"On\". Stop.",
			"3. Assume that the lights are off.",
			"4. Print out the string \"Off\". Stop.",
			)
		]

		for subtitle in subtitles:
			subtitle.scale(0.66)

		for line in (*linearProgram, *nonlinearProgram):
			line.scale(0.50)

		mainTitle.to_edge(UP)

		for subtitle in subtitles:
			subtitle.next_to(mainTitle, DOWN).shift(0.25*DOWN)

		subtitleF.next_to(subtitleE, DOWN)
		subtitleG.next_to(subtitleE, DOWN)

		codeA.to_edge(RIGHT).shift(0.5*DOWN)
		outputA.next_to(codeA, DOWN).align_to(codeA, LEFT)
		outputB.next_to(codeA, DOWN).align_to(codeA, LEFT)

		codeAExplained[0].to_edge(LEFT).align_to(codeA, UP)

		for i in range(1, len(codeAExplained)):
			codeAExplained[i].next_to(codeAExplained[i-1], DOWN).to_edge(LEFT)

		linearProgram[0].next_to(subtitleA, DOWN).shift(0.25*DOWN).to_edge(LEFT)
		nonlinearProgram[0].next_to(subtitleA, DOWN).shift(0.25*DOWN).to_edge(LEFT)

		actors = [mainTitle]

		self.play(Write(mainTitle))

		# Linear Program

		tmpactors = [subtitleA, linearProgram[0]]

		for actor in tmpactors:
			self.wait(1)
			self.play(Write(actor))

		for i in range(1, len(linearProgram)):
			linearProgram[i].next_to(linearProgram[i-1], DOWN).to_edge(LEFT)
			tmpactors.append(linearProgram[i])
			self.wait(1)
			self.play(Write(linearProgram[i]))

		self.wait(1)
		tmpactors.remove(subtitleA)
		self.play(FadeOut(subtitleA))
		tmpactors.append(subtitleB)
		self.play(Write(subtitleB))

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in tmpactors])

		# Non-Linear Program

		tmpactors = [subtitleA, nonlinearProgram[0]]

		for actor in tmpactors:
			self.wait(1)
			self.play(Write(actor))

		for i in range(1, len(nonlinearProgram)):
			nonlinearProgram[i].next_to(nonlinearProgram[i-1], DOWN).to_edge(LEFT)
			tmpactors.append(nonlinearProgram[i])
			self.wait(1)
			self.play(Write(nonlinearProgram[i]))

		self.wait(1)
		tmpactors.remove(subtitleA)
		self.play(FadeOut(subtitleA))
		tmpactors.append(subtitleC)
		self.play(Write(subtitleC))

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in tmpactors])

		# Python

		tmpactors = [subtitleE, codeA, *codeAExplained]

		for actor in tmpactors:
			self.wait(1)
			self.play(Write(actor))

		# I don't bother putting these in tmpactors because life is futile.

		self.wait(1)
		self.play(Write(subtitleF))

		self.wait(1)
		self.play(Write(outputA[:2]))
		self.wait(1)
		self.play(Write(outputA[2][0]))

		highlightsA = [SurroundingRectangle(line, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0, buff=0.05) for line in (
			# Dumb fix for tabs.
			codeA[2][0], codeA[2][1][1:]
			)
		]

		self.wait(1)
		self.play(Write(highlightsA[0]))

		self.wait(1)
		self.play(Transform(highlightsA[0], highlightsA[1]))
		self.play(Write(outputA[2][1]))

		self.wait(1)
		self.play(*[FadeOut(actor) for actor in (outputA, highlightsA[0], subtitleF)])

		self.wait(1)
		self.play(Write(subtitleG))

		self.wait(1)
		self.play(Write(outputB[:2]))
		self.wait(1)
		self.play(Write(outputB[2][0]))

		highlightsB = [
			SurroundingRectangle(line, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0, buff=0.05) for line in [
				# Dumb fix for tabs.
				codeA[2][0], codeA[2][2], codeA[2][3][1:]
			]
		]

		self.wait(1)
		self.play(Write(highlightsB[0]))

		self.wait(1)
		self.play(Transform(highlightsB[0], highlightsB[1]))

		self.wait(1)
		self.play(Transform(highlightsB[0], highlightsB[2]))
		self.play(Write(outputB[2][1]))

		self.wait(1)
		self.play(*[FadeOut(actor) for actor in (outputB, highlightsB[0], subtitleG)])

		# Cleanup.

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in [*tmpactors, *actors]])

