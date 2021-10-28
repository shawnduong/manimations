from manim import *

class s03b_Object_Oriented_Programming(Scene):

	def construct(self):

		# Actors.
		title = Text("Object-Oriented Programming")
		point = Text("What if we have abstract ideas that we would like to\n"
			+ "represent as fundamentally discrete but similar real items?").scale(0.66)
		code = [
			Code(
				file_name="./code/s03b_s0.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			).scale(0.75),
			Code(
				file_name="./code/s03b_s1.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			).scale(0.66),
		]
		remarks = [
			Text("The solution is to\nabstract them as classes!").scale(0.50),
			Text("Classes are \"blueprints\" that are the basis of objects.").scale(0.50),
			Text("First we define a\nclass (-ification).").scale(0.50),
			Text("This can have attributes.").scale(0.50),
			Text("This can have methods.").scale(0.50),
		]

		# Positioning.
		title.to_edge(UP+LEFT)
		point.next_to(title, DOWN).to_edge(LEFT)
		code[0].next_to(point, DOWN)
		remarks[0].set_z_index(-1)
		remarks[1].to_edge(DOWN).shift(0.50*UP)

		# Modifiers.
		ul = Underline(title)

		# Animations.

		actors = [title, ul, point]

		for i in range(len(actors)):

			self.play(Write(actors[i]))

			if i > 1:
				self.wait(0.5)

		self.play(Write(code[0]))
		self.wait(0.5)

		self.add(remarks[0])
		self.play(ApplyMethod(code[0].shift, 3.50*LEFT), ApplyMethod(remarks[0].shift, 3.50*RIGHT))
		self.wait(0.5)

		code[1].move_to(code[0], UP+LEFT)
		actors.append(code[1])
		self.play(Write(code[1]))
		self.remove(code[0])
		self.wait(0.5)

		actors.append(remarks[1])
		self.play(Write(remarks[1]))
		self.wait(0.5)

		# Highlights after transformation of code[1].
		highlights = [
			Rectangle(fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0,
				height=2.00, width=6.30),
			Rectangle(fill_color="#0000CC", fill_opacity=0.25, stroke_width=0,
				height=0.50, width=2.30),
			Rectangle(fill_color="#0000CC", fill_opacity=0.25, stroke_width=0,
				height=0.75, width=5.70),
		]

		# Positioning after transformation of code[1] and remarks[0].
		remarks[2].move_to(remarks[0])
		highlights[0].align_to(code[1][2], UP+LEFT)
		highlights[0].shift(0.1*UP + 0.1*LEFT)
		highlights[1].align_to(highlights[0], UP+LEFT)
		highlights[1].shift(0.5*DOWN + 0.5*RIGHT)
		highlights[2].align_to(highlights[1], UP+LEFT)
		highlights[2].shift(0.62*DOWN)

		actors.append(highlights[0])
		actors.append(remarks[2])
		self.play(FadeOut(remarks[0]))
		self.play(Write(highlights[0]), Write(remarks[2]))
		self.wait(0.5)

		actors.append(highlights[1])
		actors.append(remarks[3])
		self.play(ApplyMethod(remarks[2].shift, 1*UP))
		remarks[3].next_to(remarks[2], DOWN)
		remarks[3].shift(0.5*DOWN)
		remarks[4].next_to(remarks[3], DOWN)
		self.play(Write(highlights[1]), Write(remarks[3]))
		self.wait(0.5)

		actors.append(highlights[2])
		actors.append(remarks[4])
		self.play(Write(highlights[2]), Write(remarks[4]))
		self.wait(0.5)

		# Cleanup.
		self.wait(0.5)
		self.play(*[FadeOut(actor) for actor in actors if actor not in (title, ul)])

