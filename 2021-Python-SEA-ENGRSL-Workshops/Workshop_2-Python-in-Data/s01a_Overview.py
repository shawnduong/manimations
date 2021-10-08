from manim import *

class s01a_Overview(Scene):

	def construct(self):

		# Actors.

		mainTitle = Text("Overview")
		subtitleA = Text("Objectives")
		subtitleB = Text("Agenda")

		objectives = [
			Text("1. Continue developing a programmatic mindset."),
			Text("2. Explore another application of Python."),
			Text("3. Become comfortable writing basic Python code."),
		]

		agenda = [
			Text("- For Loops"),
			Text("- Functions"),
			Text("- Libraries"),
			Text("- Demo: matplotlib"),
			Text("- Activity: Generating a Line Graph"),
		]

		# Scaling.

		subtitleA.scale(0.66)
		subtitleB.scale(0.66)

		for objective in objectives:
			objective.scale(0.66)

		for item in agenda:
			item.scale(0.66)

		# Positioning.

		mainTitle.to_edge(UP)
		subtitleA.next_to(mainTitle, DOWN).to_edge(LEFT)
		objectives[0].next_to(subtitleA, DOWN).to_edge(LEFT)

		for i in range(1, len(objectives)):
			objectives[i].next_to(objectives[i-1], DOWN).to_edge(LEFT)

		subtitleB.next_to(objectives[-1], DOWN).to_edge(LEFT)
		agenda[0].next_to(subtitleB, DOWN).to_edge(LEFT)

		for i in range(1, len(agenda)):
			agenda[i].next_to(agenda[i-1], DOWN).to_edge(LEFT)

		# Animations.

		actors = [mainTitle, subtitleA, *objectives, subtitleB, *agenda]

		self.play(Write(mainTitle))
		self.play(*[Write(sub) for sub in (subtitleA, subtitleB)])
		self.wait(1)
		self.play(*[Write(obj) for obj in objectives])
		self.wait(1)
		self.play(*[Write(itm) for itm in agenda])

		# Cleanup.

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in actors])

