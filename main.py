import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='Input file path')
parser.add_argument('-o', '--output_file', help='Output file path', default='./out.js')
args = parser.parse_args()

# print(f"Input file path: {args.input_file}")
# print(f"Output file path: {args.output_file}")

compiled_code = ""

with open(args.input_file, 'r') as f:
	lines = f.readlines()


for line in lines:
	# TODO: do something with lines
	line = "".join(line.splitlines())
	if line[0:4] == "say,": 
		compiled_code += f"console.log(\"{line[4:]}\");\n"
	elif line[0:5] == "hear,":
		compiled_code += f"prompt(\"{line[5:]}\")"
	else:
		compiled_code += "console.log(\"a\")"

with open(args.output_file, 'w') as f:
	f.write(compiled_code)
