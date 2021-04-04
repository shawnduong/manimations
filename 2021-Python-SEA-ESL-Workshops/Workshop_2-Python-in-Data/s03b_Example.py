from manim import *

class s03b_Example(Scene):

	def construct(self):

		# Actors.

		mainTitle = Text("Example")
		subtitles = [
			Text("Consider the following code."),
		]

		code = Code(
			file_name="./code/s03b_s0.py",
			tab_width=4,
			font="Monospace",
			background="window",
			style="monokai",
			language="python",
		)

		output = Code(
			file_name="./code/s03b_o0.txt",
			tab_width=4,
			font="Monospace",
			background="window",
			insert_line_no=False,
			style="monokai",
			language="text",
		)

		annotations = [
			Text("A function with 1 output is being defined."), # 0
			Text("A list with 10 items is being defined."),     # 1
			Text("The function is called with 2 inputs."),      # 2
			Text("The output of the function is printed."),     # 3
		]

		counter = Tex("i = ")
		values = [Tex(f"{x}") for x in range(7+1)]

		# Scaling.

		for subtitle in subtitles:
			subtitle.scale(0.66)

		for annotation in annotations:
			annotation.scale(0.50)

		counter.scale(0.75)

		for val in values:
			val.scale(0.75)

		# Positioning.

		mainTitle.to_edge(UP)

		for subtitle in subtitles:
			subtitle.next_to(mainTitle, DOWN)

		output.next_to(code, DOWN).align_to(code, LEFT)

		for annotation in annotations:
			annotation.next_to(output, RIGHT).align_to(output, UP)

		counter.next_to(annotations[0], DOWN).align_to(annotations[0], LEFT)

		for val in values:
			val.next_to(counter, RIGHT)

		# Highlights.

		codeHighlights = [SurroundingRectangle(line, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0, buff=0.05) for line in (
			code[2][0], code[2][2][1:], code[2][3][2:], code[2][4][3:], code[2][6], code[2][7], code[2][8],
			# 0         1               2               3               4           5           6
			)
		]

		funcHighlights = [SurroundingRectangle(line, color="#00FFFF", fill_color="#00FFFF", fill_opacity=0.25, stroke_width=0, buff=0.05) for line in (
			code[2][0], code[2][2][1:], code[2][3][2:], code[2][4][3:],
			# 0         1               2               3
			)
		]

		listHighlights = [SurroundingRectangle(item, color="#00FFFF", fill_color="#00FFFF", fill_opacity=0.25, stroke_width=0, buff=0.05) for item in (
			code[2][6][11], code[2][6][14], code[2][6][17], code[2][6][20], code[2][6][23], code[2][6][26], code[2][6][29], code[2][6][32:34]
			# 0 (0)         1 (1)           2 (1)           3 (2)           4 (3)           5 (5)           6 (8)           7 (13)
			)
		]

		# Animations. 

		actors = []

		actors.append(mainTitle)
		self.play(Write(mainTitle))
		self.wait(1)

		actors.append(subtitles[0])
		self.play(Write(subtitles[0]))
		self.wait(1)

		actors.append(code)
		self.play(Write(code))

		actors.append(output)
		self.play(Write(output[:2]))
		self.play(Write(output[2][0]))
		self.wait(1)

		actors.append(codeHighlights[0])
		self.play(Write(codeHighlights[0]))
		actors.append(annotations[0])
		self.play(Write(annotations[0]))
		self.wait(1)

		for i in range(1, len(codeHighlights)):

			self.play(Transform(codeHighlights[0], codeHighlights[i]))

			if i == 4:

				actors.remove(annotations[0])
				self.play(FadeOut(annotations[0]))
				actors.append(annotations[1])
				self.play(Write(annotations[1]))

			elif i == 5:

				actors.remove(annotations[1])
				self.play(FadeOut(annotations[1]))
				actors.append(annotations[2])
				self.play(Write(annotations[2]))

				# Breakdown of the function call.

				actors.append(funcHighlights[0])
				self.play(Write(funcHighlights[0]))
				self.wait(1)

				# i = 0
				self.play(Transform(funcHighlights[0], funcHighlights[1]))
				actors.append(counter)
				self.play(Write(counter))
				actors.append(values[0])
				self.play(Write(values[0]))
				self.wait(1)
				self.play(Transform(funcHighlights[0], funcHighlights[2]))
				actors.append(listHighlights[0])
				self.play(Write(listHighlights[0]))
				self.wait(1)

				# i = 1
				self.play(Transform(funcHighlights[0], funcHighlights[1]))
				self.play(Transform(values[0], values[1]))
				self.wait(1)
				self.play(Transform(funcHighlights[0], funcHighlights[2]))
				self.play(Transform(listHighlights[0], listHighlights[1]))
				self.wait(1)

				# i = 2
				self.play(Transform(funcHighlights[0], funcHighlights[1]))
				self.play(Transform(values[0], values[2]))
				self.wait(1)
				self.play(Transform(funcHighlights[0], funcHighlights[2]))
				self.play(Transform(listHighlights[0], listHighlights[2]))
				self.wait(1)

				# i = 3
				self.play(Transform(funcHighlights[0], funcHighlights[1]))
				self.play(Transform(values[0], values[3]))
				self.wait(1)
				self.play(Transform(funcHighlights[0], funcHighlights[2]))
				self.play(Transform(listHighlights[0], listHighlights[3]))
				self.wait(1)

				# i = 4
				self.play(Transform(funcHighlights[0], funcHighlights[1]))
				self.play(Transform(values[0], values[4]))
				self.wait(1)
				self.play(Transform(funcHighlights[0], funcHighlights[2]))
				self.play(Transform(listHighlights[0], listHighlights[4]))
				self.wait(1)

				# i = 5
				self.play(Transform(funcHighlights[0], funcHighlights[1]))
				self.play(Transform(values[0], values[5]))
				self.wait(1)
				self.play(Transform(funcHighlights[0], funcHighlights[2]))
				self.play(Transform(listHighlights[0], listHighlights[5]))
				self.wait(1)

				# i = 6
				self.play(Transform(funcHighlights[0], funcHighlights[1]))
				self.play(Transform(values[0], values[6]))
				self.wait(1)
				self.play(Transform(funcHighlights[0], funcHighlights[2]))
				self.play(Transform(listHighlights[0], listHighlights[6]))
				self.wait(1)

				# i = 7
				self.play(Transform(funcHighlights[0], funcHighlights[1]))
				self.play(Transform(values[0], values[7]))
				self.wait(1)
				self.play(Transform(funcHighlights[0], funcHighlights[2]))
				self.play(Transform(listHighlights[0], listHighlights[7]))
				self.wait(1)
				self.play(Transform(funcHighlights[0], funcHighlights[3]))
				self.wait(1)

				actors.remove(funcHighlights[0])
				actors.remove(listHighlights[0])
				actors.remove(counter)
				actors.remove(values[0])
				self.play(*[FadeOut(actor) for actor in (funcHighlights[0], listHighlights[0], counter, values[0])])
				self.wait(1)

			elif i == 6:

				self.play(Write(output[2][1]))
				actors.remove(annotations[2])
				self.play(FadeOut(annotations[2]))
				actors.append(annotations[3])
				self.play(Write(annotations[3]))

			self.wait(1)

		actors.remove(codeHighlights[0])
		self.play(FadeOut(codeHighlights[0]))

		# Cleanup.

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in actors])

