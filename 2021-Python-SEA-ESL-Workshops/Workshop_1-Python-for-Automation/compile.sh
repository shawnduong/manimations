#!/bin/sh

echo ":: Preparing for a fresh render..."
rm -r media/ 2>/dev/null

echo ":: Rendering scenes..."

manim s00a_Title.py
manim s01a_Overview.py
manim s02a_The_Bigger_Picture.py
manim s03a_Basic_Data_Types.py
manim s03b_Output.py
manim s03c_Elaborated.py
manim s04a_Control_Flow_Statements.py
manim s04b_Demonstration.py
manim s04c_Control_Flow_Statements.py
manim s04d_For_Loops.py
manim s05a_Demo_Programmatic_Thinking.py
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
