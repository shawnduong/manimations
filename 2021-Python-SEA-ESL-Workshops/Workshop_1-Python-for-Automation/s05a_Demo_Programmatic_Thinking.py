from manim import *

class s05a_Demo_Programmatic_Thinking(GraphScene):

	def __init__(self, **kwargs):

		GraphScene.__init__(
			self,
			x_min=-1,
			x_max=5,
			y_min=-1,
			y_max=12,
			x_axis_width=5,
			y_axis_height=4.5,
			graph_origin=ORIGIN,
			axes_color=BLUE,
			x_labeled_nums=range(0, 5, 1),
			y_labeled_nums=range(0, 12, 1),
			**kwargs
		)

		self.function_color = WHITE

	def construct(self):

		mainTitle = Text("Demo: Programmatic Thinking")
		subtitleA = Text("Create a program that calculates the area under the curve.")

		subtitleA.scale(0.66)

		mainTitle.to_edge(UP)
		subtitleA.next_to(mainTitle, DOWN)

		actors = [mainTitle, subtitleA]

		for actor in actors:
			self.play(Write(actor))
			self.wait(1)

		# Graphing the function.

		self.graph_origin = 2.75*DOWN + 5*LEFT
		self.setup_axes(animate=True)
		actors.append(self.axes)

		function = lambda x: x**2

		fGraph = self.get_graph(function, self.function_color, x_min=self.x_min, x_max=3.5)
		fLabel = self.get_graph_label(fGraph, label="f(x) = x^2", x_val=3.5)

		actors.append(fGraph)
		actors.append(fLabel)
		self.play(ShowCreation(fGraph))
		self.play(Write(fLabel))

		# Defining the domain.

		# Texs are smaller.
		commentA = Tex("Suppose we only want the area from 0 to 3.")

		commentA.scale(0.66)
		commentA.shift(3.25*RIGHT + 0.90*UP)

		self.wait(1)
		actors.append(commentA)
		self.play(Write(commentA))

		domainLine = self.get_vertical_line_to_graph(3, fGraph, DashedLine, color=YELLOW)
		areaShaded = self.get_area(fGraph, 0, 3, area_color=YELLOW)

		self.wait(1)
		actors.append(domainLine)
		actors.append(areaShaded)
		self.play(Write(domainLine))
		self.play(Write(areaShaded))

		# Instructions for Riemann sums.

		commentB = Tex("We can calculate the areas of small rectangles inside.")

		commentB.scale(0.50)
		commentB.next_to(commentA, DOWN).align_to(commentA, LEFT)

		self.wait(1)
		actors.append(commentB)
		self.play(Write(commentB))

		self.wait(1)
		self.play(FadeOut(areaShaded))

		instructions = [Tex(t) for t in (
			"1. Let $A = 0, x* = 0, dx = 1$.",
			"2. While $x* < 3$, continue.",
			"3. Add $f(x*) \\times dx$ to $A$.",
			"4. Add $dx$ to $x*$.",
			"5. Go back to step 2.",
			)
		]

		for actor in instructions:
			actors.append(actor)
			actor.scale(0.50)

		instructions[0].next_to(commentB, DOWN).align_to(commentB, LEFT)

		for i in range(1, len(instructions)):
			instructions[i].next_to(instructions[i-1], DOWN).align_to(instructions[0], LEFT)

		for actor in instructions:
			self.wait(1)
			self.play(Write(actor))

		varA = Tex("$A$")
		varX = Tex("$x*$")
		eqlA = Tex("$=$")
		eqlX = Tex("$=$")
		valA = [Tex(a) for a in ("0", "0", "1", "5")]
		valX = [Tex(x) for x in ("0", "1", "2", "3")]

		tmpactors = [varA, varX, eqlA, eqlX, valA[0], valX[0]]

		varA.next_to(instructions[-1]).shift(0.75*DOWN).align_to(instructions[-1], LEFT)
		varX.next_to(varA, DOWN).align_to(varA, LEFT)

		eqlA.next_to(varA, RIGHT)
		eqlX.next_to(varX, RIGHT)
		eqlA.align_to(eqlX, LEFT)

		for a in valA:
			a.next_to(eqlA, RIGHT)

		for x in valX:
			x.next_to(eqlX, RIGHT)

		self.play(*[FadeIn(actor) for actor in (varA, varX, eqlA, eqlX)])

		# Doing the Riemann sums.

		rectangles  = self.get_riemann_rectangles(fGraph, x_min=0, x_max=3, dx=1, input_sample_type="left")
		highlights  = [SurroundingRectangle(line, fill_color="#FFFF00", fill_opacity=0.25, stroke_width=0) for line in instructions]
		highlighter = highlights[0].copy()

		# Index     0  1  2  3  4  5  6  7  8  9 10 11 12 13
		sequence = (0, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1)

		self.wait(1)
		self.play(Write(highlighter))
		self.play(Write(valA[0]), Write(valX[0]))

		for i in range(1, len(sequence)):

			self.wait(1)
			self.play(Transform(highlighter, highlights[sequence[i]]))

			if i == 2:
				self.play(Write(rectangles[0]))
				self.play(Transform(valA[0], valA[1]))

			elif i == 3:
				self.play(Transform(valX[0], valX[1]))

			elif i == 6:
				self.play(Write(rectangles[1]))
				self.play(Transform(valA[0], valA[2]))

			elif i == 7:
				self.play(Transform(valX[0], valX[2]))

			elif i == 10:
				self.play(Write(rectangles[2]))
				self.play(Transform(valA[0], valA[3]))

			elif i == 11:
				self.play(Transform(valX[0], valX[3]))

		self.wait(1)
		self.play(FadeOut(highlighter))

		self.wait(1)
		self.play(*[FadeOut(actor) for actor in (*tmpactors, *rectangles)])

		# Final notes.

		noteA = Tex("As $dx$ approaches $0$, we get the true area.")
		noteB = Tex("Let's have a look at the Python code for this.")

		for actor in (noteA, noteB):
			actors.append(actor)
			actor.scale(0.50)

		noteA.next_to(instructions[-1], DOWN).align_to(instructions[-1], LEFT)
		noteB.next_to(noteA, DOWN).align_to(noteA, LEFT)

		actors.append(noteA)
		actors.append(noteB)

		self.wait(1)
		self.play(Write(noteA))
		self.play(Write(areaShaded))

		self.wait(1)
		self.play(Write(noteB))

		# Cleanup.

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in actors])

