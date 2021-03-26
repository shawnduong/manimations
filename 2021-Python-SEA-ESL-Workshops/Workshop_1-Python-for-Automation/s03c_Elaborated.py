from manim import *

class s03c_Elaborated(Scene):

	def construct(self):

		mainTitle = Text("Basic Data Types")
		subtitles = [
			Text("Strings"),   # 0
			Text("Integers"),  # 1
			Text("Floats"),    # 2
			Text("Booleans"),  # 3
			Text("Lists"),     # 4
			Text("Tuples"),    # 5
		]
		captions = [
			Text("(Composite)"), # 0
			Text("(Primitive)"), # 1
			Text("(Primitive)"), # 2
			Text("(Primitive)"), # 3
			Text("(Composite)"), # 4
			Text("(Composite)"), # 5
		]

		mainTitle.to_edge(UP)

		for subtitle in subtitles:
			subtitle.scale(0.75)
			subtitle.next_to(mainTitle, DOWN).shift(0.5*DOWN)

		for i in range(len(captions)):
			captions[i].scale(0.66)
			captions[i].next_to(subtitles[i], DOWN)

		actors = [mainTitle]

		self.play(Write(mainTitle))

		# Strings

		string = "\"Hello World!\""
		strtxt = Text(string).scale(0.66)
		chrtxt = Text(" ".join([f"'{c}'" for c in string[1:-1]]) + " '\\0'").scale(0.50)
		bintxt = Text("".join([bin(ord(c))[2:].zfill(8) for c in string[1:10]]) + "...").scale(0.25)
		tmpactors = []

		self.wait(1)
		tmpactors.append(subtitles[0])
		tmpactors.append(captions[0])
		self.play(Write(subtitles[0]))
		self.play(Write(captions[0]))

		strtxt.to_edge(LEFT)
		chrtxt.next_to(strtxt, DOWN).to_edge(LEFT)
		bintxt.next_to(chrtxt, DOWN).to_edge(LEFT)

		highlight = SurroundingRectangle(strtxt, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0)

		self.wait(1)
		tmpactors.append(strtxt)
		self.play(Write(strtxt))

		self.wait(1)
		tmpactors.append(chrtxt)
		self.play(Write(chrtxt))

		self.wait(1)
		tmpactors.append(bintxt)
		self.play(Write(bintxt))

		self.wait(1)
		tmpactors.append(highlight)
		self.play(Write(highlight))

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in tmpactors])

		# Integers

		number = "20"
		inttxt = Text(number).scale(0.66)
		bintxt = Text(bin(int(number))[2:].zfill(32)).scale(0.50)
		tmpactors = []

		self.wait(1)
		tmpactors.append(subtitles[1])
		tmpactors.append(captions[1])
		self.play(Write(subtitles[1]))
		self.play(Write(captions[1]))

		inttxt.to_edge(LEFT)
		bintxt.next_to(inttxt, DOWN).to_edge(LEFT)

		highlight = SurroundingRectangle(inttxt, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0)

		self.wait(1)
		tmpactors.append(inttxt)
		self.play(Write(inttxt))

		self.wait(1)
		tmpactors.append(bintxt)
		self.play(Write(bintxt))

		self.wait(1)
		tmpactors.append(highlight)
		self.play(Write(highlight))

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in tmpactors])

		# Floats

		number = "3.14"
		binary = "01000000010010001111010111000011"
		inttxt = Text(number).scale(0.66)
		bintxt = Text(binary).scale(0.50)
		tmpactors = []

		self.wait(1)
		tmpactors.append(subtitles[2])
		tmpactors.append(captions[2])
		self.play(Write(subtitles[2]))
		self.play(Write(captions[2]))

		inttxt.to_edge(LEFT)
		bintxt.next_to(inttxt, DOWN).to_edge(LEFT)

		highlight = SurroundingRectangle(inttxt, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0)

		self.wait(1)
		tmpactors.append(inttxt)
		self.play(Write(inttxt))

		self.wait(1)
		tmpactors.append(bintxt)
		self.play(Write(bintxt))

		self.wait(1)
		tmpactors.append(highlight)
		self.play(Write(highlight))

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in tmpactors])

		# Booleans

		boolFa = "False"
		boolTr = "True"
		faltxt = Text(boolFa).scale(0.66)
		trutxt = Text(boolTr).scale(0.66)
		biftxt = Text("0").scale(0.50)
		bittxt = Text("1").scale(0.50)
		tmpactors = []

		self.wait(1)
		tmpactors.append(subtitles[3])
		tmpactors.append(captions[3])
		self.play(Write(subtitles[3]))
		self.play(Write(captions[3]))

		faltxt.to_edge(LEFT)
		biftxt.next_to(faltxt, DOWN).to_edge(LEFT)
		trutxt.next_to(biftxt, DOWN).to_edge(LEFT)
		bittxt.next_to(trutxt, DOWN).to_edge(LEFT)

		highlightA = SurroundingRectangle(faltxt, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0)
		highlightB = SurroundingRectangle(trutxt, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0)

		self.wait(1)
		tmpactors.append(faltxt)
		self.play(Write(faltxt))

		self.wait(1)
		tmpactors.append(biftxt)
		self.play(Write(biftxt))

		self.wait(1)
		tmpactors.append(trutxt)
		self.play(Write(trutxt))

		self.wait(1)
		tmpactors.append(bittxt)
		self.play(Write(bittxt))

		self.wait(1)
		tmpactors.append(highlightA)
		self.play(Write(highlightA))
		tmpactors.append(highlightB)
		self.play(Write(highlightB))

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in tmpactors])

		# Lists

		# I'm not even gonna bother renaming my variables here...
		string = "[100, 80, 75, 60, 98]"
		strtxt = Text(string).scale(0.66)
		chrtxt = Text("    ".join([f"{c}" for c in string[1:-1].split(", ")])).scale(0.50)
		bintxt = Text("Low-level implementation varies across languages.").scale(0.50)
		tmpactors = []

		self.wait(1)
		tmpactors.append(subtitles[4])
		tmpactors.append(captions[4])
		self.play(Write(subtitles[4]))
		self.play(Write(captions[4]))

		strtxt.to_edge(LEFT)
		chrtxt.next_to(strtxt, DOWN).to_edge(LEFT)
		bintxt.next_to(chrtxt, DOWN).to_edge(LEFT)

		highlight = SurroundingRectangle(strtxt, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0)

		self.wait(1)
		tmpactors.append(strtxt)
		self.play(Write(strtxt))

		self.wait(1)
		tmpactors.append(chrtxt)
		self.play(Write(chrtxt))

		self.wait(1)
		tmpactors.append(bintxt)
		self.play(Write(bintxt))

		self.wait(1)
		tmpactors.append(highlight)
		self.play(Write(highlight))

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in tmpactors])

		# Lists

		# I'm not even gonna bother renaming my variables here...
		string = "('red', 'green', 'blue')"
		strtxt = Text(string).scale(0.66)
		chrtxt = Text("      ".join([f"{c}" for c in string[1:-1].split(", ")])).scale(0.50)
		bintxt = Text("Low-level implementation varies across languages.").scale(0.50)
		tmpactors = []

		self.wait(1)
		tmpactors.append(subtitles[5])
		tmpactors.append(captions[5])
		self.play(Write(subtitles[5]))
		self.play(Write(captions[5]))

		strtxt.to_edge(LEFT)
		chrtxt.next_to(strtxt, DOWN).to_edge(LEFT)
		bintxt.next_to(chrtxt, DOWN).to_edge(LEFT)

		highlight = SurroundingRectangle(strtxt, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0)

		self.wait(1)
		tmpactors.append(strtxt)
		self.play(Write(strtxt))

		self.wait(1)
		tmpactors.append(chrtxt)
		self.play(Write(chrtxt))

		self.wait(1)
		tmpactors.append(bintxt)
		self.play(Write(bintxt))

		self.wait(1)
		tmpactors.append(highlight)
		self.play(Write(highlight))

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in tmpactors])

		# Cleanup.

		self.wait(1)
		self.play(*[FadeOut(actor) for actor in actors])

