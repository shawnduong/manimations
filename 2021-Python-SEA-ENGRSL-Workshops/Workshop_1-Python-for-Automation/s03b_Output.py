from manim import *

class s03b_Output(Scene):

	def construct(self):

		mainTitle = Text("Output")
		subtitleA = Text("The print function will write data to the screen.")

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

		subtitleA.scale(0.66)
		code.scale(0.9)
		output.scale(0.9)

		mainTitle.to_edge(UP)
		subtitleA.next_to(mainTitle, DOWN)
		code.to_edge(LEFT).shift(1*DOWN)
		output.to_edge(RIGHT).align_to(code, UP)

		highlights = [SurroundingRectangle(line, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0, buff=0.05) for line in code[2]]

		actors = [mainTitle, subtitleA, code, output[:2], output[2][0]]

		for actor in actors:
			self.play(Write(actor))
			self.wait(1)

		self.play(FadeIn(highlights[0]))
		self.wait(1)

		skips = [6]
		mapping = {
			 7: 1,
			 8: 2,
			 9: 3,
			10: 4,
			11: 5,
			12: 6,
		}

		for i in range(1, len(highlights)):

			if i in skips:
				continue

			self.play(Transform(highlights[0], highlights[i]))

			if i in mapping.keys():
				actors.append(output[2][mapping[i]])
				self.play(Write(output[2][mapping[i]]))

			self.wait(1)

		self.play(FadeOut(highlights[0]))

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in actors])

