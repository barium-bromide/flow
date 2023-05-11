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
    line = line.strip()
    token = line.split(" ")
    if token[-1].endswith(";"):
        token[-1] = token[-1][:-1] 
        if token[0] == "say":
            compiled_code += f'console.log(\"{" ".join(token[1:])}\");\n'
        elif token[0] in ("str", "num", "bool"):
            var_token = "".join(token[1:]).split("=", 1)
            if token[0] == "str":
                compiled_code += f'let {var_token[0]} = \"{var_token[1]}\";\n'
            elif token[0] == "num" and var_token[1].isnumeric():
                compiled_code += f'let {var_token[0]} = {var_token[1]};\n'
            elif token[0] == "bool" and var_token[1] in ("true", "false"):
                compiled_code += f'let {var_token[0]} = {var_token[1]};\n'

with open(args.output_file, 'w') as f:
	f.write(compiled_code)
