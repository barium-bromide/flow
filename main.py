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
	line = line.strip()
	token = line.split(" ")
	if token[0] == "say" and token[-1][-1] == ";":
		token[-1] = token[-1][:-1] + ""
		compiled_code += f'console.log(\"{" ".join(token[1:])}\");\n'
	elif token[0] in ("bool", "str", "num") and token[-1][-1] == ";":
			token[-1] = token[-1][:-1] + ""
			var_token = "".join(token[1:]).split("=")
			if token[0] == "str":
				compiled_code += f'let {var_token[0]} = \"{"=".join(var_token[1:])}\";\n'
			elif token[0] == "num":
				if "=".join(var_token[1:]).isnumeric():
					compiled_code += f'let {var_token[0]} = {"=".join(var_token[1:])};\n'
			elif token[0] == "bool":
				if "=".join(var_token[1:]) in ("true", "false"):
					compiled_code += f'let {var_token[0]} = {"=".join(var_token[1:])};\n'

with open(args.output_file, 'w') as f:
	f.write(compiled_code)
