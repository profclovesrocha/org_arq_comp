import tkinter as tk
import random

# Lista de desenhos da forca baseados nos erros (0 até 6)
ESTAGIOS_FORCA = [
    """
       +---+
       |   |
           |
           |
           |
           |
     =========
    """,  # 0 erros
    """
       +---+
       |   |
       O   |
           |
           |
           |
     =========
    """,  # 1 erro (Cabeça)
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========
    """,  # 2 erros (Tronco)
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========
    """,  # 3 erros (Um braço)
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
     =========
    """,  # 4 erros (Dois braços)
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
     =========
    """,  # 5 erros (Uma perna)
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
     =========
    """   # 6 erros (Enforcou!)
]

# Lista de palavras
banco_de_palavras = ['python', 'algoritmo', 'programacao', 'computador', 'logica']
palavra_secreta = random.choice(banco_de_palavras)

letras_acertadas = ['_' for _ in palavra_secreta]
# Mudado para 6 tentativas para encaixar com o desenho completo do boneco
tentativas = 6 
letras_digitadas = []

# Função principal
def verificar_letra():
    global tentativas

    chute = entrada.get().lower().strip()
    entrada.delete(0, tk.END)

    # Se o jogo já acabou, não faz nada
    if "_" not in letras_acertadas or tentativas == 0:
        return

    # Validação
    if len(chute) != 1 or not chute.isalpha():
        resultado.config(text="Digite apenas uma letra válida!")
        return

    if chute in letras_digitadas:
        resultado.config(text="Você já tentou essa letra!")
        return

    letras_digitadas.append(chute)

    if chute in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == chute:
                letras_acertadas[i] = chute
        resultado.config(text=f"Boa! A letra '{chute}' está na palavra.")
    else:
        tentativas -= 1
        resultado.config(text=f"Errou! A letra '{chute}' não está.")

    atualizar_tela()

# Atualiza a interface
def atualizar_tela():
    palavra_label.config(text=" ".join(letras_acertadas))
    tentativas_label.config(text=f"Tentativas restantes: {tentativas}")
    letras_label.config(text=f"Letras usadas: {', '.join(letras_digitadas)}")
    
    # Atualiza o desenho da forca (calcula o estágio baseado nos erros)
    erros = 6 - tentativas
    forca_label.config(text=ESTAGIOS_FORCA[erros])

    if "_" not in letras_acertadas:
        resultado.config(text="🎉 Você ganhou!")
        botao.config(state="disabled")
        entrada.config(state="disabled") # Desativa a entrada ao ganhar

    elif tentativas == 0:
        resultado.config(text=f"😢 Você perdeu! Palavra: {palavra_secreta}")
        botao.config(state="disabled")
        entrada.config(state="disabled") # Desativa a entrada ao perder

# Criar janela
janela = tk.Tk()
janela.title("Jogo da Forca")
janela.geometry("450x550") # Aumentei um pouco o tamanho para caber o desenho à vontade

# Título
titulo = tk.Label(janela, text="JOGO DA FORCA", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Componente Visual da Forca (Usa fonte Courier para o texto não entortar)
forca_label = tk.Label(janela, text=ESTAGIOS_FORCA[0], font=("Courier", 12), justify="left")
forca_label.pack()

# Palavra
palavra_label = tk.Label(janela, text=" ".join(letras_acertadas), font=("Arial", 20))
palavra_label.pack(pady=10)

# Entrada
entrada = tk.Entry(janela, font=("Arial", 14), justify="center", width=5)
entrada.pack()
entrada.focus() # Já abre a janela com o cursor piscando na caixinha

# Vincula a tecla ENTER do teclado à função do jogo
janela.bind('<Return>', lambda event: verificar_letra())

# Botão
botao = tk.Button(janela, text="Tentar letra", command=verificar_letra)
botao.pack(pady=10)

# Tentativas
tentativas_label = tk.Label(janela, text=f"Tentativas restantes: {tentativas}", font=("Arial", 10))
tentativas_label.pack()

# Letras usadas
letras_label = tk.Label(janela, text="Letras usadas: ", font=("Arial", 10))
letras_label.pack()

# Resultado
resultado = tk.Label(janela, text="", font=("Arial", 12, "bold"))
resultado.pack(pady=10)

# Rodar
janela.mainloop()