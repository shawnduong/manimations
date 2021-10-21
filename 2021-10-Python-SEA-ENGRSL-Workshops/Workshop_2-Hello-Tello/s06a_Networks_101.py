from manim import *

class s06a_Networks_101(Scene):

	def construct(self):

		# Actors.
		title = Text("Networks 101")
		objects = {
			"computer1" : ImageMobject("./img/computer.png"),
			"computer2" : ImageMobject("./img/computer.png"),
			"switch"    : ImageMobject("./img/switch.png").scale(0.75),
			"wap"       : ImageMobject("./img/wap.png").scale(0.75),
		}

		# Positioning.
		title.to_edge(UP)
		objects["switch"].shift(1*UP)
		objects["wap"].align_to(objects["switch"], DOWN)

		# Modifiers.
		ul = Underline(title)

		# Animations.

		actors = [title, ul]

		for actor in actors:
			self.play(Write(actor))

		actors.append(objects["computer1"])
		self.wait(0.5)
		self.play(FadeIn(objects["computer1"]))

		actors.append(objects["computer2"])
		self.wait(0.5)
		self.play(
			ApplyMethod(objects["computer1"].shift, 3*LEFT),
			ApplyMethod(objects["computer2"].shift, 3*RIGHT),
		)

		# Temporary actors.
		wire = Line(objects["computer1"].get_center(), objects["computer2"].get_center()).shift(0.5*DOWN)
		msg1 = Text("Hey there!").scale(0.25)
		msg2 = Text("Hello yourself!").scale(0.25)
		temp = [wire, msg1, msg2]

		msg1.move_to(wire.get_corner(UP+RIGHT)).shift(0.1*UP)
		msg2.move_to(wire.get_corner(UP+LEFT)).shift(0.1*UP)
		wire.set_z_index(-1)
		msg1.set_z_index(-1)
		msg2.set_z_index(-1)

		self.wait(0.5)
		self.play(Write(wire))

		self.wait(0.5)
		self.play(ApplyMethod(msg1.shift, 2*LEFT))

		self.wait(0.5)
		self.play(ApplyMethod(msg1.shift, 4*LEFT))

		self.wait(0.5)
		self.play(ApplyMethod(msg2.shift, 2*RIGHT))

		self.wait(0.5)
		self.play(ApplyMethod(msg2.shift, 4*RIGHT))

		self.wait(0.5)
		self.play(*[FadeOut(actor) for actor in temp])

		self.wait(0.5)
		self.play(
			ApplyMethod(objects["computer1"].shift, 2*DOWN),
			ApplyMethod(objects["computer2"].shift, 2*DOWN),
			FadeIn(objects["switch"]),
		)

		# More temporary actors.
		# These 3 lines make up a wire.
		line1 = Line(
			objects["computer1"].get_center() + 3*UP,
			objects["computer1"].get_center(),
		).shift(0.25*RIGHT)
		line2 = Line(
			objects["computer2"].get_center(),
			objects["computer2"].get_center() + 3*UP,
		).shift(0.25*LEFT)
		line3 = Line(line2.get_corner(UP+RIGHT), line1.get_corner(UP+LEFT))
		msg1 = Text("Ping!").scale(0.25)
		msg2 = Text("Pong!").scale(0.25)

		msg1.move_to(line2.get_corner(DOWN+RIGHT)).shift(0.50*RIGHT)
		msg2.move_to(line1.get_corner(DOWN+LEFT)).shift(0.50*LEFT)

		line1.set_z_index(-1)
		line2.set_z_index(-1)
		line3.set_z_index(-1)
		msg1.set_z_index(-1)
		msg2.set_z_index(-1)

		temp = [line1, line2, line3, msg1, msg2]

		self.wait(0.5)
		self.play(Write(line2))
		self.play(Write(line3))
		self.play(Write(line1))

		self.wait(0.5)
		self.play(ApplyMethod(msg1.shift, 3.20*UP))
		self.play(ApplyMethod(msg1.shift, 3*LEFT))
		self.wait(0.5)
		self.play(ApplyMethod(msg1.shift, 3.50*LEFT))
		self.play(ApplyMethod(msg1.shift, 3.20*DOWN))

		self.wait(0.5)
		self.play(ApplyMethod(msg2.shift, 3.20*UP))
		self.play(ApplyMethod(msg2.shift, 3*RIGHT))
		self.wait(0.5)
		self.play(ApplyMethod(msg2.shift, 3.50*RIGHT))
		self.play(ApplyMethod(msg2.shift, 3.20*DOWN))

		self.wait(0.5)
		self.play(*[FadeOut(actor) for actor in temp])

		actors.append(objects["wap"])
		self.wait(0.5)
		self.play(FadeOut(objects["switch"]), FadeIn(objects["wap"]))

		self.wait(0.5)
		msg1.move_to(line2.get_corner(DOWN+RIGHT)).shift(0.50*RIGHT)
		msg2.move_to(line1.get_corner(DOWN+LEFT)).shift(0.50*LEFT)

		self.play(ApplyMethod(msg1.shift, 3.20*UP))
		self.play(ApplyMethod(msg1.shift, 3*LEFT))
		self.wait(0.5)
		self.play(ApplyMethod(msg1.shift, 3.50*LEFT))
		self.play(ApplyMethod(msg1.shift, 3.20*DOWN))

		self.wait(0.5)
		self.play(ApplyMethod(msg2.shift, 3.20*UP))
		self.play(ApplyMethod(msg2.shift, 3*RIGHT))
		self.wait(0.5)
		self.play(ApplyMethod(msg2.shift, 3.50*RIGHT))
		self.play(ApplyMethod(msg2.shift, 3.20*DOWN))

		self.remove(msg1)
		self.remove(msg2)

		# Cleanup.
		self.wait(0.5)
		self.play(*[FadeOut(actor) for actor in actors])

