import codecs
import sys

if len(sys.argv) < 2:
    print("Invalid argument!")
    sys.exit(1)

input_filename = sys.argv[1]

try:
    with codecs.open(input_filename, mode="r", encoding="utf-8") as input_file:
        lines = input_file.readlines()
except UnicodeDecodeError:
    with codecs.open(input_filename, mode="r", encoding="utf-16le") as input_file:
        lines = input_file.readlines()

output_lines = set()

with open('out.txt', mode="w", encoding="utf-8") as output_file:
    for line in lines:
        if "avc: denied" in line:
            denied_text = line.split("avc: denied")[1].strip()
            if denied_text not in output_lines:
                output_file.write(line.strip() + "\n")
                output_lines.add(denied_text)
