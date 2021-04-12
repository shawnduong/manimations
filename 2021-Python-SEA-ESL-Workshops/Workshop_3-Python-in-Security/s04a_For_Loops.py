from manim import *

class s04a_For_Loops(Scene):

	def construct(self):

		# Actors.

		mainTitle = Text("Review: For Loops")
		subtitles = [
			Text("Consider the following instructions."),               # 0
			Text("This is a looping program."),                         # 1
			Text("Consider the following instructions."),               # 2
			Text("This is a looping program, but with simpler logic."), # 3
			Text("Consider the following program."),                    # 4
		]

		whileProgram = [Text(line) for line in (
			"1. Gather the past 4 hourly temperatures.",
			"2. While the list of temperatures is not empty, continue. Else, stop.",
			"3. Go to a temperature in the list.",
			"4. Output it in Celsius.",
			"5. Remove it from the list.",
			"6. Go back to step 2.",
			)
		]

		forProgram = [Text(line) for line in (
			"1. Gather the past 4 hourly temperatures.",
			"2. For every temperature, output it in Celsius."
			)
		]

		code = Code(
			file_name="./code/s04a_s0.py",
			tab_width=4,
			font="Monospace",
			background="window",
			style="monokai",
			language="python",
		)

		output = Code(
			file_name="./code/s04a_o0.txt",
			tab_width=4,
			font="Monospace",
			background="window",
			insert_line_no=False,
			style="monokai",
			language="text",
		)

		# Scaling.

		for subtitle in subtitles:
			subtitle.scale(0.66)

		for line in (*whileProgram, *forProgram):
			line.scale(0.50)

		# Positioning.

		mainTitle.to_edge(UP)

		for subtitle in subtitles:
			subtitle.next_to(mainTitle, DOWN).shift(0.25*DOWN)

		whileProgram[0].next_to(subtitles[0], DOWN).shift(0.25*DOWN).to_edge(LEFT)
		forProgram[0].next_to(subtitles[0], DOWN).shift(0.25*DOWN).to_edge(LEFT)

		for i in range(1, len(whileProgram)):
			whileProgram[i].next_to(whileProgram[i-1], DOWN).align_to(whileProgram[i-1], LEFT)

		for i in range(1, len(forProgram)):
			forProgram[i].next_to(forProgram[i-1], DOWN).align_to(forProgram[i-1], LEFT)

		code.to_edge(RIGHT).align_to(forProgram[0], UP)
		code.next_to(forProgram[-1], DOWN).shift(1*DOWN).to_edge(LEFT)
		output.next_to(code, RIGHT).align_to(code, DOWN)

		# Animations.

		actors = [mainTitle]

		for actor in actors:
			self.play(Write(actor))
			self.wait(1)

		# While program.

		tmpactors = [subtitles[0], *whileProgram]

		for actor in tmpactors:
			self.play(Write(actor))
			self.wait(1)

		tmpactors.remove(subtitles[0])
		self.play(FadeOut(subtitles[0]))

		tmpactors.append(subtitles[1])
		self.play(Write(subtitles[1]))
		self.wait(1)

		self.play(*[FadeOut(actor) for actor in tmpactors])
		self.wait(1)

		# For program.

		tmpactors = [subtitles[2], *forProgram]

		for actor in tmpactors:
			self.play(Write(actor))
			self.wait(1)

		tmpactors.remove(subtitles[2])
		self.play(FadeOut(subtitles[2]))

		tmpactors.append(subtitles[3])
		self.play(Write(subtitles[3]))
		self.wait(1)

		tmpactors.remove(subtitles[3])
		self.play(FadeOut(subtitles[3]))

		tmpactors.append(subtitles[4])
		self.play(Write(subtitles[4]))
		self.wait(1)

		tmpactors.append(code)
		self.play(Write(code))

		tmpactors.append(output)
		self.play(Write(output[:2]))
		self.play(Write(output[2][0]))
		self.wait(1)

		highlights = [SurroundingRectangle(line, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0, buff=0.05) for line in (
			code[2][0], code[2][2], code[2][3][1:], code[2][2], code[2][3][1:], code[2][2], code[2][3][1:], code[2][2], code[2][3][1:],
			# 0         1           2               3           4               5           6               7           8
			)
		]

		highlightsB = [SurroundingRectangle(line, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0, buff=0.05) for line in (
			code[2][0][9:11], code[2][0][13:15], code[2][0][17:19], code[2][0][21:23],
			)
		]

		mappings = {
			2: output[2][1],
			4: output[2][2],
			6: output[2][3],
			8: output[2][4],
		}

		self.play(Write(highlights[0]))
		self.wait(1)

		for i in range(1, len(highlights)):

			self.play(Transform(highlights[0], highlights[i]))

			if i in mappings.keys():
				self.play(Write(mappings[i]))

			if i == 1:
				self.play(Write(highlightsB[0]))
				c = 0

			if i in (3, 5, 7):
				c += 1
				self.play(Transform(highlightsB[0], highlightsB[0+c]))

			self.wait(1)

		self.play(FadeOut(highlightsB[0]))
		self.play(FadeOut(highlights[0]))
		self.wait(1)

		# Cleanup.

		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in (*tmpactors, *actors)])

