from manim import *

class s03c_Object_Oriented_Programming(Scene):

	def construct(self):

		# Actors.
		title = Text("Object-Oriented Programming")
		point = Text("OOP is the idea that things can be represented abstractly\n"
			+ "as classes, instantiated as objects, and interacted with.").scale(0.66)
		objects = {
			"apple"  : ImageMobject("./img/apple.png").scale(0.80),
			"apple1" : ImageMobject("./img/apple1.png").scale(0.78),
			"apple2" : ImageMobject("./img/apple.png").scale(0.64),
			"apple3" : ImageMobject("./img/apple3.png").scale(0.80),
			"apple4" : ImageMobject("./img/apple1.png").scale(0.76),
		}

		# Positioning.
		title.to_edge(UP+LEFT)
		point.next_to(title, DOWN).to_edge(LEFT)

		# Modifiers.
		ul = Underline(title)

		# Animations.

		self.add(title)
		self.add(ul)

		actors = [title, ul, point]

		self.play(Write(point))
		self.wait(0.5)

		actors.append(objects["apple"])
		self.play(FadeIn(objects["apple"]))
		self.wait(0.5)

		for i in range(1, len(objects.keys())):
			actor = objects[list(objects.keys())[i]]
			actors.append(actor)
			actor.set_z_index(-1)
			self.play(ApplyMethod(actor.move_to, [-7.6 + 3*i, -2.5, 0]))

		self.wait(0.5)

		# Cleanup.
		self.wait(0.5)
		self.play(*[FadeOut(actor) for actor in actors])

