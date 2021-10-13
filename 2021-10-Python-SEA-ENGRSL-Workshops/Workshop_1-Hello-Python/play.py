#!/usr/bin/env python3

import cv2
import time

from termcolor import colored

# Set this to true if you want to find checkpoints.
DEFINEMODE = True

# Playback speed.
SPEED = 2

def main():

	# Make the display window fullscreen.
	cv2.namedWindow("Display", cv2.WND_PROP_FULLSCREEN)
	cv2.setWindowProperty("Display", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

	# Open up the video and get the framerate.
	mp4 = cv2.VideoCapture("./render/FINAL.mp4")
	fps = int(mp4.get(cv2.CAP_PROP_FPS)) * SPEED

	# Make sure that it's open.
	assert mp4.isOpened, "Video doesn't exist. Is it in ./render/FINAL.mp4?"

	# Counter for the frame number.
	n = 0

	# Checkpoints of n to pause at.
	checkpoints = [int(n.strip("\n")) for n in open("./checkpoints.txt", "r").readlines()]

	# Paused switch.
	paused = False

	# Loop to show.
	while mp4.isOpened():

		# Show the frame if not paused.
		if not paused:

			ret, frame = mp4.read()

			# Display the frame.
			if ret:
				cv2.imshow("Display", frame)
				time.sleep(1/fps)
			else:
				break

		# Grab a key if pressed.
		key = cv2.waitKey(1) & 0xFF

		# Pause at designated checkpoints.
		if n in checkpoints:
			if not paused:
				print(f":: Hit breakpoint {checkpoints.index(n)}.")
				print(colored(":: Pausing.", "red"))
				paused = True

		# Press 'q' to quit.
		if key == ord('q'):

			print(colored(":: 'q' detected. Are you sure you want to quit?", "red"))
			print(colored(":: -> Type 'yes' in the controller console to quit.", "red"))

			if (input(":: >> ") == 'yes'):
				print(colored(":: Quitting.", "red"))
				break

			else:
				print(colored(":: Playing.", "green"))

		# Press ' ' to manually pause or unpause.
		elif key == ord(' '):
			if not paused:
				print(colored(":: Pausing.", "red"))
				paused = True
			else:
				print(colored(":: Playing.", "green"))
				paused = False

		# Press RIGHT to go to the next checkpoint.
		elif key == 83:
			print(colored(":: Going FORWARD a checkpoint.", "green"))
			paused = False

		# Press LEFT to go to the previous checkpoint.
		elif key == 81:

			print(colored(":: Going BACKWARD a checkpoint.", "red"))

			for i in range(n-1, -1, -1):

				print(colored(f"=> i={i}", "red"))

				if i in checkpoints:

					mp4.set(cv2.CAP_PROP_POS_FRAMES, i-1)
					n = i-1
					break

			ret, frame = mp4.read()

			# Display the frame.
			if ret:
				cv2.imshow("Display", frame)
				time.sleep(1/fps)
			else:
				break

			paused = False

		# Increment or decrement the frame based on status.
		if not paused:
			n += 1

		if not paused and DEFINEMODE:
			print(f"=> n={n}")

	# Release.
	mp4.release()

	# Close.
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()
