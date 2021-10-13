from manim import *

class s05b_Logic(Scene):

	def construct(self):

		# Actors.
		title = Text("Logic")
		points = VGroup(*[
			Text(x).scale(0.75) for x in (
				"Logic is the fundamental basis of programming.",
				"Consider the following instructions:",
			)
		])
		linearProgram = VGroup(*[
			Text(x).scale(0.50) for x in (
				"1. Preheat oven to 175 C.",
				"2. Cream together butter and sugar.",
				"3. Beat in eggs.",
				"4. Stir in vanilla and baking soda.",
				"5. Stir in flour and chocolate chips.",
				"6. Drop by spoonfuls into baking sheet.",
				"7. Bake for 15 minutes.",
			)
		])
		nonlinearProgram = VGroup(*[
			Text(x).scale(0.50) for x in (
				"1. Go to the first battery.",
				"2. If it is powered on, go to step 3. Else, step 4.",
				"3. Record the charge and go to step 5.",
				"4. Turn the battery on and go to step 5.",
				"5. If there is a next battery, repeat steps 2-5 for it.",
			)
		])
		footnotes = VGroup(*[
			Text(x).scale(0.75) for x in (
				"This is an example of a linear program.",
				"This is an example of a non-linear program.",
				"These are all examples of control flow structures,",
				"which are logical structures.",
			)
		])

		# Positioning.
		title.to_edge(UP+LEFT)
		points.arrange(direction=DOWN, aligned_edge=LEFT)
		points.next_to(title, DOWN).to_edge(LEFT)
		linearProgram.arrange(direction=DOWN, aligned_edge=LEFT)
		linearProgram.next_to(points, DOWN)
		nonlinearProgram.arrange(direction=DOWN, aligned_edge=LEFT)
		nonlinearProgram.next_to(points, DOWN)
		footnotes.to_edge(DOWN)

		# Opacity.
		linearProgram.set_opacity(0.50)
		nonlinearProgram.set_opacity(0.50)

		# Modifiers.
		ul = Underline(title)

		# Highlights.
		highlight = SurroundingRectangle(points[0][10:26], fill_color="#FFFF00",
			fill_opacity=0.25, stroke_width=0, buff=0.05)

		# Animations.

		actors = [title, ul, points[0], highlight, points[1]]

		self.play(Write(actors[0]))
		self.play(Write(actors[1]))
		self.wait(1)

		self.play(Write(actors[2]))
		self.play(Write(actors[3]))
		self.wait(1)

		self.play(Write(actors[4]))
		self.wait(1)

		self.play(Write(linearProgram))
		self.wait(1)

		for line in linearProgram:
			self.play(ApplyMethod(line.set_opacity, 1.00))
			self.wait(1)
			self.play(ApplyMethod(line.set_opacity, 0.50))

		self.play(Write(footnotes[0]))
		self.wait(1)

		self.play(*[FadeOut(x) for x in [linearProgram, footnotes[0]]])
		self.wait(1)

		actors.append(nonlinearProgram)
		self.play(Write(nonlinearProgram))
		self.wait(1)

		for line in nonlinearProgram:
			self.play(ApplyMethod(line.set_opacity, 1.00))
			self.wait(1)
			self.play(ApplyMethod(line.set_opacity, 0.50))

		actors.append(footnotes[1])
		self.play(Write(footnotes[1]))
		self.wait(1)

		self.play(ApplyMethod(footnotes[1].shift, 1.1*UP))
		footnotes[2].next_to(footnotes[1], DOWN)
		footnotes[3].next_to(footnotes[2], DOWN)

		actors.append(footnotes[2])
		actors.append(footnotes[3])
		self.play(Write(footnotes[2]))
		self.play(Write(footnotes[3]))
		self.wait(1)

		# Cleanup.
		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

