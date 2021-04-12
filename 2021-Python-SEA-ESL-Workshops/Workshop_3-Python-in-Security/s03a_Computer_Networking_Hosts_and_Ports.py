from manim import *

class s03a_Computer_Networking_Hosts_and_Ports(Scene):

	def construct(self):

		# Actors.

		mainTitle = Text("Computer Networking Hosts and Ports")
		imgServer = ImageMobject("./img/server.png")

		hostname = Text("123.45.67.89")
		services = [Text(service) for service in ("FTP", "SSH", "SMTP", "HTTP", "HTTPS")]
		ports = [Text(port) for port in ("tcp/21", "tcp/22", "tcp/25", "tcp/80", "tcp/443")]

		# Scaling.

		imgServer.scale(0.50)
		hostname.scale(0.50)

		for service in services:
			service.scale(0.50)

		for port in ports:
			port.scale(0.50)

		# Positioning.

		mainTitle.to_edge(UP)
		imgServer.shift(1*UP)

		hostname.next_to(imgServer, UP)

		for i in range(-2, 2+1):
			services[i+2].shift(i*2*RIGHT + 2*DOWN)
			ports[i+2].next_to(services[i+2], DOWN)

		# Pointers.

		pointers = [Arrow(start=imgServer.get_bottom(), end=services[i].get_top()) for i in range(len(services))]

		# Animations.

		actors = []

		actors.append(mainTitle)
		self.play(Write(mainTitle))
		self.wait(1)

		actors.append(imgServer)
		self.play(FadeIn(imgServer))
		self.wait(1)

		actors.append(hostname)
		self.play(Write(hostname))
		self.wait(1)

		for i in range(len(services)):
			actors.append(services[i])
			self.play(Write(services[i]))
			actors.append(ports[i])
			self.play(Write(ports[i]))
			actors.append(pointers[i])
			self.play(Write(pointers[i]))
			self.wait(1)

		# Cleanup.

		self.wait(3-1)
		self.play(*[FadeOut(actor) for actor in actors])

