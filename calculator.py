""" Grammar:

expression = term {("+" | "-") term}.
term       = factor {("*" | "/" | "%") factor}.
factor     = number | "(" expression ")".
number     = digit {digit}.
digit      = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9".

"""
import re

raw_input = input()
print("> ", raw_input)

number_or_symbol = re.compile('(\d+|[^ 0-9])')
tokens = re.findall(number_or_symbol, raw_input)
#print(f"$ {tokens}")

i = 0
def skip_token():
    global i
    i += 1
#Ключевые места поставить print что там происходит/ Разобрать калькулятор по косточкам и можно обучать другого/
#трассировка/обработка скобки(проилюстрировать)/скобки [] поставить в нужные места

def token():
    if i < len(tokens):
#        print("i: [i] token: tokens[i]")  #Переделать токен чтобы, было красиво с помощью [].
        return tokens[i]
    else:
        return "end"


def expression():
    value = term()
#    ower = token()
    while token() == "+" or token() == "-":
        if token() == "+":
            skip_token()
            value += term()
        elif token() == "-":
            skip_token()
            value -= term()
#    print("experession.value: value")
    return value


def term():
    value = factor()
    tkn = token()
    while tkn == "*" or tkn == "/" or tkn == "%":
        if tkn == "*":
            skip_token()
            value *= factor()
        elif tkn == "/":
            skip_token()
            value /= factor()
        elif tkn == "%":
            skip_token()
            value %= factor()
#    print("term.value: value")
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
            print("Error: misplaced token()")
            #    print("factor.value: value")
        return value


print(": ", expression())
if token() != "end":
    print("Error: extra token()")


"""

''' Grammar:

expression = term {("+" | "-") term}.
term       = factor {("*" | "/" | "%") factor}.
factor     = number | "(" expression ")".
number     = digit {digit}.
digit      = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9".

'''
import re

raw_input = input()
print("> ", raw_input)

number_or_symbol = re.compile('(\d+|[^ 0-9])')
tokens = re.findall(number_or_symbol, raw_input)
#print(f"$ {tokens}")

i = 0
def skip_token():
    global i
    i += 1
#Ключевые места поставить print что там происходит/ Разобрать калькулятор по косточкам и можно обучать другого/
#трассировка/обработка скобки(проилюстрировать)/скобки [] поставить в нужные места

def token():
    if i < len(tokens):
#        print("i: [i] token: tokens[i]")  #Переделать токен чтобы, было красиво с помощью [].
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
#    print("experession.value: value")
    return value


def term():
    value = factor()
    while token() == "*" or token() == "/" or token() == "%":
        if token() == "*":
            skip_token()
            value *= factor()
        elif token() == "/":
            skip_token()
            value /= factor()
        elif token() == "%":
            skip_token()
            value %= factor()
#    print("term.value: value")
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
           print("Error: misplaced token()")
#    print("factor.value: value")
    return value


print(": ", expression())
if token() != "end":
    print("Error: extra token()")

"""
