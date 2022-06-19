rm -rf output.png
curl -s $1 | rembg i -a -ae 15 > output.png
