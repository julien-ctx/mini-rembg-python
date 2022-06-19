from rembg import remove
import sys

if len(sys.argv) != 3:
    print("Bad number of arguments")
    exit()

input_path = sys.argv[1]
output_path = sys.argv[2]

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)
