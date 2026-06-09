def ula(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b != 0:
            return a / b
        return "Erro: divisão por zero"
    elif operacao == "AND":
        return a & b
    elif operacao == "OR":
        return a | b
    elif operacao == "XOR":
        return a ^ b
    else:
        return "Operação inválida"