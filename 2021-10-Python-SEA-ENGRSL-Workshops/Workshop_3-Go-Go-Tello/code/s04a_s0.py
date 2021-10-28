#!/usr/bin/env python3

import re
import requests

# Define the steganographic encoding.
ENCODING = {
	"&#x200B": "0", # Zero-width space
	"&#xFEFF": "1", # Zero-width no-break space
}

# Define the number base.
BASE = 2

def main():

	# Get the page and extract the steganographic data.
	html = requests.get("https://shawnd.xyz/blog/uploads/2021-04-01/demo.html").content.decode()
	steg = "".join(re.compile("<p>(.+?)</p>").findall(html))

	# Extract the zero-width characters and decode them.

	extracted = ""

	for char in steg.split(";"):
		if char in ENCODING.keys():
			extracted += ENCODING[char]

	# Split the extracted data into 8-bit bytes and decode them.

	chunks = [extracted[8*i:8*(i+1)] for i in range(len(extracted)//8)]
	...
