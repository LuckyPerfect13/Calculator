""" Grammar:

expression = term {("+" | "-") term}.
term       = factor {("*" | "/") factor}.
factor     = number | "(" expression ")".
number     = digit {digit}.
digit      = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9".

"""
import re

raw_input = input()
print(f"> {raw_input}")

number_or_symbol = re.compile('(\d+|[^ 0-9])')
tokens = re.findall(number_or_symbol, raw_input)
print(f"$ {tokens}")

i = 0
def skip_token():
    global i
    i += 1

def token():
    if i < len(tokens):
        return tokens[i]
    else:
        return "end"


def expression():
    value = term()
    while token() == "+" or token() == "-":
        if token() == "+":
            skip_token()
            value += term()
        elif token() == "-":
            skip_token()
            value -= term()
    return value


def term():
    value = factor()
    while token() == "*" or token() == "/":
        if token() == "*":
            skip_token()
            value *= factor()
        elif token() == "/":
            skip_token()
            value /= factor()
    return value


def factor():
    value = 0
    if token().isdigit():
        value = int(token())
        skip_token()
    else:
        if token() == "(":
            skip_token()
            value = expression()
            if token() == ")":
                skip_token()
            else:
                print("Error: missing ')'")
        else:
            print(f"Error: misplaced {token()}")
    return value


print(f": {expression()}")
if token() != "end":
    print(f"Error: extra {token()}")
