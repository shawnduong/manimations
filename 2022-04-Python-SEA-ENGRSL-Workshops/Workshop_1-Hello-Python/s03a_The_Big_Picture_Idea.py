from manim import *

class s03a_The_Big_Picture_Idea(Scene):

	def construct(self):

		# Actors.
		title = Text("The Big Picture Idea")
		objects = {
			"person"    : ImageMobject("./img/person.png"),
			"actions"   : ImageMobject("./img/actions.png"),
			"work"      : ImageMobject("./img/work.png"),
			"computer"  : ImageMobject("./img/computer.png"),
			"binary"    : Text(
				"01100010 01100101 01100101\n" +
				"01110000 00100000 01100010\n" +
				"01101111 01101111 01110000\n" +
				"00100000 01101001 00100111\n" +
				"01101101 00100000 01100100\n" +
				"01101111 01101001 01101110\n" +
				"01100111 00100000 01110011\n" +
				"01110100 01110101 01100110\n"
			).scale(0.20),
			"code"      : Code(
				file_name="./code/s03a_s0.py",
				tab_width=4,
				font="Monospace",
				background="window",
				style="monokai",
				language="python",
			).scale(0.30),
		}
		description = Text(
			"A source code language consists\n" + 
			"of syntax and semantics."
		).scale(0.50)

		# Positioning.
		title.to_edge(UP+LEFT)
		objects["actions"].shift(2*LEFT)
		objects["work"].shift(2*LEFT + 2*DOWN)
		objects["computer"].to_edge(LEFT)
		objects["binary"].to_edge(DOWN).shift(2*LEFT + 0.5*UP)
		objects["code"].to_edge(DOWN).shift(2*RIGHT + 0.5*UP)
		description.set_z_index(-1)

		# Modifiers.
		ul = Underline(title)

		# Animations.

		actors = [title, ul, *objects.values()]

		self.play(Write(title))
		self.play(Write(ul))
		self.wait(1)

		self.play(FadeIn(objects["person"]))
		self.wait(1)

		self.play(
			ApplyMethod(objects["person"].shift, 2*RIGHT),
			FadeIn(objects["actions"]))
		self.wait(1)

		self.play(
			ApplyMethod(objects["actions"].shift, 1.5*UP),
			FadeIn(objects["work"]))
		self.wait(1)

		# Temporary set of actors.
		pointers = {
			("person", "work") : Arrow(
				start=objects["person"].get_corner(DOWN+LEFT),
				end=objects["work"].get_right()
			),
			("work", "actions") : Arrow(
				start=objects["work"].get_top(),
				end=objects["actions"].get_bottom()
			),
			("actions", "person") : Arrow(
				start=objects["actions"].get_right(),
				end=objects["person"].get_corner(UP+LEFT)
			),
		}

		self.play(Write(pointers[("person", "work")]))
		self.play(Write(pointers[("work", "actions")]))
		self.play(Write(pointers[("actions", "person")]))
		self.wait(1)

		self.play(*[FadeOut(pointer) for pointer in pointers.values()])
		self.play(
			ApplyMethod(objects["person"].to_edge, RIGHT),
			ApplyMethod(objects["actions"].shift, 4*RIGHT),
			ApplyMethod(objects["work"].shift, 3.5*UP),
		)
		self.wait(1)

		# Temporary set of actors.
		pointers = {
			("person", "code") : Arrow(
				start=objects["person"].get_corner(DOWN+LEFT),
				end=objects["code"].get_right()
			),
			("code", "binary") : Arrow(
				start=objects["code"].get_left(),
				end=objects["binary"].get_right()
			),
			("binary", "computer") : Arrow(
				start=objects["binary"].get_left(),
				end=objects["computer"].get_corner(DOWN+RIGHT)
			),
			("computer", "work") : Arrow(
				start=objects["computer"].get_corner(UP+RIGHT),
				end=objects["work"].get_left()
			),
			("work", "actions") : Arrow(
				start=objects["work"].get_right(),
				end=objects["actions"].get_left(),
			),
			("actions", "person") : Arrow(
				start=objects["actions"].get_right(),
				end=objects["person"].get_corner(UP+LEFT)
			),
		}

		for pointer in pointers.values():
			actors.append(pointer)

		self.play(Write(pointers[("work", "actions")]))
		self.play(Write(pointers[("actions", "person")]))
		self.wait(1)

		self.play(FadeIn(objects["computer"]))
		self.wait(1)

		self.play(Write(pointers[("computer", "work")]))
		self.wait(1)

		self.play(FadeIn(objects["binary"]))
		self.wait(1)

		self.play(Write(pointers[("binary", "computer")]))
		self.wait(1)

		self.play(FadeIn(objects["code"]))
		self.wait(1)

		self.play(Write(pointers[("person", "code")]))
		self.wait(1)

		self.play(Write(pointers[("code", "binary")]))
		self.wait(1)

		# Partial cleanup.
		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors if actor != objects["code"]])
		self.wait(1)

		actors = [objects["code"]]

		self.play(ApplyMethod(objects["code"].move_to, [0, 0, 0]))
		self.play(ApplyMethod(objects["code"].scale, 2.00))
		self.wait(1)

		actors.append(description)
		self.add(description)

		self.play(
			ApplyMethod(objects["code"].shift, 3*LEFT),
			ApplyMethod(description.shift, 3*RIGHT)
		)
		self.wait(1)

		# Cleanup.
		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

