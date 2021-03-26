from manim import *

class s01a_Overview(Scene):

	def construct(self):

		mainTitle = Text("Overview")
		subtitleA = Text("Objectives")
		subtitleB = Text("Agenda")

		objectives = [
			Text("1. Understand what computer programming is."),
			Text("2. Develop a programmatic problem-solving mindset."),
			Text("3. Become comfortable reading Python code."),
		]

		agenda = [
			Text("- The Bigger Picture"),
			Text("- Basic Data Types"),
			Text("- Control Flow Statements"),
			Text("- Demo: Programmatic Thinking"),
			Text("- Activity: Automate Work Tasks"),
		]

		subtitleA.scale(0.66)
		subtitleB.scale(0.66)

		for objective in objectives:
			objective.scale(0.66)

		for item in agenda:
			item.scale(0.66)

		mainTitle.to_edge(UP)
		subtitleA.next_to(mainTitle, DOWN).to_edge(LEFT)
		objectives[0].next_to(subtitleA, DOWN).to_edge(LEFT)

		for i in range(1, len(objectives)):
			objectives[i].next_to(objectives[i-1], DOWN).to_edge(LEFT)

		subtitleB.next_to(objectives[-1], DOWN).to_edge(LEFT)
		agenda[0].next_to(subtitleB, DOWN).to_edge(LEFT)

		for i in range(1, len(agenda)):
			agenda[i].next_to(agenda[i-1], DOWN).to_edge(LEFT)

		actors = [mainTitle, subtitleA, *objectives, subtitleB, *agenda]

		self.play(Write(mainTitle))
		self.play(*[Write(sub) for sub in (subtitleA, subtitleB)])
		self.wait(1)
		self.play(*[Write(obj) for obj in objectives])
		self.wait(1)
		self.play(*[Write(itm) for itm in agenda])

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in actors])

