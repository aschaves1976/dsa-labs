# -*- coding: utf-8 -*-
# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):

        self.s_word = word
        self.s_rigth_answer = ""
        self.s_rigth_letters = ""
        self.s_wrong_letters = ""

        self.l_build_word = []
        self.l_wrong_word = []
        self.l_match_word = []
        self.n_brdind = 0
        self.n_auxind = 0

        for i in range(len(self.s_word)):
            self.l_build_word.append("_ ")

        self.print_game_status()
        self.hide_word()

    # Método para adivinhar a letra
    def guess(self, letter):

        match_letter = self.s_word.count(letter)

        if match_letter != 0:
            self.l_match_word.append(letter)
            self.n_auxind += 1

            for i, v in enumerate(self.s_word):
                if letter == v:
                    self.l_build_word[i] = v
            self.hide_word()

        else:
            self.l_wrong_word.append(letter)
            self.n_brdind += 1
            self.n_auxind = self.n_brdind

            self.print_game_status()
            self.hide_word()

    # Método para verificar se o jogo terminou
    def hangman_over(self):

        if self.hangman_won():
            return True
        elif self.n_brdind >= (len(board) - 1):
            return True
        else:
            return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if self.s_rigth_answer == self.s_word:
            return True
        else:
            return False

    # Método para não mostrar a letra no board
    def hide_word(self):

        self.s_rigth_answer = "".join(self.l_build_word)

        if len(self.l_match_word) > 0:
            self.s_rigth_letters = ", ".join(self.l_match_word)

        if len(self.l_wrong_word) > 0:
            self.s_wrong_letters = ", ".join(self.l_wrong_word)

        print("\nPalavra: {}".format(str(self.s_rigth_answer)))
        print("\nLetras erradas: {}".format(self.s_wrong_letters))
        print("\nLetras corretas: {}".format(self.s_rigth_letters))

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        if self.n_brdind == self.n_auxind:
            print(board[self.n_brdind])


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    # strip() é utilizado para retirar espaços a esquerda e a direita da palavra
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        letter = input("\nDigite uma letra: ")
        game.guess(letter)

    # Verifica o status do jogo
    # game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.s_word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
