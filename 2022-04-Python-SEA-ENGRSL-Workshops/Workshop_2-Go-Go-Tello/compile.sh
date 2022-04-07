#!/bin/sh

echo ":: Preparing for a fresh render..."
rm -r media/ 2>/dev/null

echo ":: Rendering scenes..."
for file in $(ls ./*.py); do
	python -m manim $file
done

echo ":: Concatenating scenes..."
mkdir -p ./render/scenes/
mv ./media/videos/*/1080p60/*.mp4 ./render/scenes/
ls -1 ./render/scenes/*.mp4 > ./tmp.txt
sed "s/.*/file '&'/" ./tmp.txt > ./playlist.txt
rm ./tmp.txt
ffmpeg -f concat -safe 0 -i ./playlist.txt -c copy ./render/FINAL.mp4

echo ":: Final video written to ./render/FINAL.mp4"
echo ":: Done."
