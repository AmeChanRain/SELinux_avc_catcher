import sys

if len(sys.argv) < 2:
    print("Invalid argument!")
    sys.exit(1)

input_filename = sys.argv[1]

with open(input_filename, 'r') as input_file:
    with open('out.txt', 'w') as output_file:
        for line in input_file:
            if 'avc: denied' in line:
                output_file.write(line)
