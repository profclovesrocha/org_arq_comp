def ula(A, B, opcode):
    
    if opcode == 0:
        resultado = A + B

    elif opcode == 1:
        resultado = A - B

    elif opcode == 2:
        resultado = A & B

    elif opcode == 3:
        resultado = A | B

    elif opcode == 4:
        resultado = A ^ B

    elif opcode == 5:
        resultado = ~A

    elif opcode == 6:
        resultado = A << 1

    elif opcode == 7:
        resultado = A >> 1

    else:
        return "Operação inválida"

    zero = 1 if resultado == 0 else 0
    sinal = 1 if resultado < 0 else 0
    carry = 1 if resultado > 255 or resultado < 0 else 0
    overflow = carry

    return {
        "Resultado": resultado,
        "Zero": zero,
        "Sinal": sinal,
        "Carry": carry,
        "Overflow": overflow
    }


print("Soma:", ula(10, 5, 0))
print("Subtração:", ula(10, 5, 1))
print("AND:", ula(10, 5, 2))
print("OR:", ula(10, 5, 3))
print("XOR:", ula(10, 5, 4))
print("NOT:", ula(10, 0, 5))
print("Shift Left:", ula(10, 0, 6))
print("Shift Right:", ula(10, 0, 7))
print("Teste Overflow:", ula(255, 1, 0))
print("Teste Zero:", ula(5, 5, 1))

input("Pressione ENTER para sair...")