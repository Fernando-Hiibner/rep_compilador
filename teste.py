from numpy import true_divide


def B(x):
    if x == "(":
        return True
    elif x == ")":
        return True
    else:
        return False

TESTE = {
    "E" : {
        "B" : lambda x : B(x)
    }
}

print(TESTE["E"]["B"]("("))
print(TESTE["E"]["B"](")"))
print(TESTE["E"]["B"]("HUR DUR MINHA BATERIA VAI ACBAR"))