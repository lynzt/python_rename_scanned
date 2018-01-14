## Synopsis

This is a script to rename files that were auto-named by a scanner.
Takes filename like: Scan.jpeg / Scan 1.jpeg
Renames to: scan_########s.jpeg


## Running

docker build -t py/rename .
docker run -it --rm -v "$PWD":/usr/src/app -v "<path>/Pictures/scanned":/tmp py/rename python3 ./rename_pics.py
