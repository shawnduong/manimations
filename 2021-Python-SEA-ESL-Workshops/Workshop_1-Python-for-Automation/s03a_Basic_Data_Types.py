from manim import *

class s03a_Basic_Data_Types(Scene):

	def construct(self):

		mainTitle = Text("Basic Data Types")
		subtitleA = Text("Data is information.")
		overtypes = [
			Text("Words"),
			Text("Numbers"),
			Text("Collections"),
		]
		subdtypes = {
			"Words": [
				Text("Strings"),
			],
			"Numbers": [
				Text("Booleans"),
				Text("Floats"),
				Text("Integers"),
			],
			"Collections": [
				Text("Tuples"),
				Text("Lists"),
			],
		}

		subtitleA.scale(0.66)

		for k in subdtypes.keys():
			for v in subdtypes[k]:
				v.scale(0.66)

		mainTitle.to_edge(UP)
		subtitleA.next_to(mainTitle, DOWN).shift(0.25*DOWN)
		overtypes[0].next_to(subtitleA, DOWN).shift(1*DOWN + 4*LEFT)
		overtypes[1].next_to(subtitleA, DOWN).shift(1*DOWN + 1*LEFT)
		overtypes[2].next_to(subtitleA, DOWN).shift(1*DOWN + 3*RIGHT)

		divider = Line(start=overtypes[0].get_corner(DOWN+LEFT), end=overtypes[-1].get_corner(DOWN+RIGHT)).shift(0.1*DOWN)

		actors = [mainTitle, subtitleA, *overtypes, divider]

		for actor in actors:
			self.play(Write(actor))
			self.wait(1)

		subdtypes["Words"][0].next_to(overtypes[0], DOWN).shift(0.25*DOWN)

		for i in range(len(subdtypes["Numbers"])):
			subdtypes["Numbers"][i].next_to(overtypes[1], DOWN).shift(0.25*DOWN)

		for i in range(len(subdtypes["Collections"])):
			subdtypes["Collections"][i].next_to(overtypes[2], DOWN).shift(0.25*DOWN)

		actors.append(subdtypes["Words"][0])
		self.play(Write(subdtypes["Words"][0]))
		self.wait(1)

		actors.append(subdtypes["Numbers"][0])
		self.play(Write(subdtypes["Numbers"][0]))
		self.wait(1)

		for i in range(1, len(subdtypes["Numbers"])):
			actors.append(subdtypes["Numbers"][i])
			self.play(
				*[ApplyMethod(subdtypes["Numbers"][j].shift, 0.66*DOWN) for j in range(i)],
				Write(subdtypes["Numbers"][i])
			)
			self.wait(1)

		actors.append(subdtypes["Collections"][0])
		self.play(Write(subdtypes["Collections"][0]))
		self.wait(1)

		for i in range(1, len(subdtypes["Collections"])):
			actors.append(subdtypes["Collections"][i])
			self.play(
				ApplyMethod(subdtypes["Collections"][i-1].shift, i*0.66*DOWN),
				Write(subdtypes["Collections"][i])
			)
			self.wait(1)

		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

