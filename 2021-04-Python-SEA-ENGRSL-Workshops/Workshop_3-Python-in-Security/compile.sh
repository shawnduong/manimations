#!/bin/sh

echo ":: Preparing for a fresh render..."
rm -r media/ 2>/dev/null

echo ":: Rendering scenes..."
manim s00a_Title.py
manim s01a_Overview.py
manim s02a_Overview_of_Workshop_Activity.py
manim s03a_Computer_Networking_Hosts_and_Ports.py
manim s04a_For_Loops.py
manim s05a_Review_Functions.py
manim s06a_Activity.py

echo ":: Concatenating scenes..."
mkdir -p ./render/scenes/
mv ./media/videos/*/1080p60/*.mp4 ./render/scenes/
ls -1 ./render/scenes/*.mp4 > ./tmp.txt
sed "s/.*/file '&'/" ./tmp.txt > ./playlist.txt
rm ./tmp.txt
ffmpeg -f concat -safe 0 -i ./playlist.txt -c copy ./render/FINAL.mp4

echo ":: Final video written to ./render/FINAL.mp4"
echo ":: Done."
