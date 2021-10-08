from manim import *

class s02a_The_Bigger_Picture(Scene):

	def construct(self):

		mainTitle = Text("The Bigger Picture")

		images = {
			"person"   : ImageMobject("./img/person.png"),
			"actions"  : ImageMobject("./img/actions.png"),
			"work"     : ImageMobject("./img/work.png"),
			"computer" : ImageMobject("./img/computer.png"),
			"binary"   : ImageMobject("./img/binary.png"),
			"code"     : ImageMobject("./img/code.png"),
		}

		mainTitle.to_edge(UP)
		images["actions"].shift(2*LEFT)
		images["work"].shift(2*LEFT + 2*DOWN)

		actors = [mainTitle, *[images[k] for k in images.keys()]]

		self.play(Write(mainTitle))

		self.wait(1)
		self.play(FadeIn(images["person"]))
		self.wait(1)
		self.play(ApplyMethod(images["person"].shift, 2*RIGHT))
		self.play(FadeIn(images["actions"]))
		self.wait(1)
		self.play(ApplyMethod(images["actions"].shift, 1.5*UP))
		self.play(FadeIn(images["work"]))

		pointersA = {
			"personToWork"    : Arrow(start=images["person"].get_corner(DOWN+LEFT), end=images["work"].get_right()),
			"workToActions"   : Arrow(start=images["work"].get_top(), end=images["actions"].get_bottom()),
			"actionsToPerson" : Arrow(start=images["actions"].get_right(), end=images["person"].get_corner(UP+LEFT)),
		}

		for k in pointersA.keys():
			actors.append(pointersA[k])

		self.wait(1)
		self.play(Write(pointersA["personToWork"]))
		self.play(Write(pointersA["workToActions"]))
		self.play(Write(pointersA["actionsToPerson"]))

		for k in pointersA.keys():
			actors.remove(pointersA[k])

		self.wait(1)
		self.play(*[FadeOut(pointersA[k]) for k in pointersA.keys()])
		self.play(
			ApplyMethod(images["person"].to_edge, RIGHT),
			ApplyMethod(images["actions"].shift, 4*RIGHT),
			ApplyMethod(images["work"].shift, 3.5*UP),
		)

		images["computer"].to_edge(LEFT)
		images["binary"].to_edge(DOWN).shift(2*LEFT + 0.5*UP)
		images["code"].to_edge(DOWN).shift(2*RIGHT + 0.5*UP)

		self.wait(1)
		self.play(FadeIn(images["computer"]))
		self.wait(1)
		self.play(FadeIn(images["binary"]))
		self.wait(1)
		self.play(FadeIn(images["code"]))

		# I'm not even gonna try to name them properly...
		pointersB = [
			Arrow(start=images["person"].get_corner(DOWN+LEFT), end=images["code"].get_right()),
			Arrow(start=images["code"].get_left(), end=images["binary"].get_right()),
			Arrow(start=images["binary"].get_left(), end=images["computer"].get_corner(DOWN+RIGHT)),
			Arrow(start=images["computer"].get_corner(UP+RIGHT), end=images["work"].get_left()),
			Arrow(start=images["work"].get_right(), end=images["actions"].get_left()),
			Arrow(start=images["actions"].get_right(), end=images["person"].get_corner(UP+LEFT)),
		]

		for pointer in pointersB:
			actors.append(pointer)
			self.wait(1)
			self.play(Write(pointer))

		self.wait(3)
		self.play(*[FadeOut(actor) for actor in actors])

