#.\run.bat run this

import argparse 
import re

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='Input file path')
parser.add_argument('-o', '--output_file', help='Output file path', default='./out.js')
args = parser.parse_args()

# print(f"Input file path: {args.input_file}")
# print(f"Output file path: {args.output_file}")

compiled_code = ""

error = None
error_msg = ""
token_list_value = []

with open(args.input_file, 'r') as f:
	lines = f.readlines()

def check_error(row, line):
    if not(line.endswith(";")):
        return True, f"; error on line {row + 1}: Please add ; at the end of the sentence."
    else:
         return None, ""

for row, line in enumerate(lines):
    if error:
         break
    line = line.strip()
    error, error_msg = check_error(row, line)
    token = line.split(" ")
    token[-1] = token[-1][:-1]
    if token[0] == ":":
        compiled_code += f'console.log(\"{" ".join(token[1:])}\");'
    elif token[0] in ("str", "num", "bool", "list"):
        var_tokens = " ".join(token[1:]).split(" = ", 1)
        if token[0] == "str":
            compiled_code += f'let {var_tokens[0]} = \"{var_tokens[1]}\";'
        elif token[0] == "num" and var_tokens[1].isnumeric():
            compiled_code += f'let {var_tokens[0]} = {var_tokens[1]};'
        elif token[0] == "bool" and var_tokens[1] in ("true", "false", "null"):
            compiled_code += f'let {var_tokens[0]} = {var_tokens[1]};'
        elif token[0] == "list":
            token_list_item = var_tokens[1].split(" ")
            for idx in range(0, len(token_list_item), 2):
                if token_list_item[idx] == "str":
                      token_list_value.append(str(token_list_item[idx + 1]))
                elif token_list_item[idx] == "num":
                     if token_list_item[idx + 1].isnumeric():
                        token_list_value.append(float(token_list_item[idx + 1]))

                 
            compiled_code += f'let {var_tokens[0]} = [{token_list_value}];'

if error:
     print(error_msg)
     compiled_code = ""

with open(args.output_file, 'w') as f:
	f.write(compiled_code)
