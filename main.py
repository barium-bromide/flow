import argparse

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
	compiled_code += "console.log(\"Hello, World!\");"

with open(args.output_file, 'w') as f:
	f.write(compiled_code)
