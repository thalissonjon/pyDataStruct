
import random

palavras = [
    "casa", "carro", "livro", "mesa", "cadeira",
    "telefone", "computador", "janela", "porta", "parede",
    "chao", "teto", "quadro", "relogio", "sofa",
    "geladeira", "fogao", "microondas", "televisao", "ventilador",
    "lampada", "tapete", "cortina", "espelho", "almofada",
    "bicicleta", "moto", "onibus", "aviao", "navio",
    "praia", "montanha", "rio", "floresta", "deserto",
    "cidade", "vila", "bairro", "estrada", "ponte",
    "parque", "jardim", "praca", "mercado", "supermercado",
    "loja", "restaurante", "cinema", "teatro", "biblioteca"
]

random.shuffle(palavras)
palavra = palavras[0]


def forca(palavra):
    palavraAcert = ''
    acertou = False
    chances = 5
    tentativas = []
    for i in range(len(palavra)):
        palavraAcert += '-'


    while not acertou or chances != 0:
        tentativa = input('Coloque sua letra: ')  
        letraAcert = False

        for i in range(len(palavra)):
            if len(tentativa) > 1:
                print('Insira apenas uma letra')          
                break

            if tentativa in tentativas:
                print('Você já tentou essa letra.')
                break

            if tentativa == palavra[i]:
                palavraAcert = palavraAcert[:i] + tentativa + palavraAcert[i+1:]
                print(f'Palavra: {palavraAcert}') 
                letraAcert = True         
            
            if i == len(palavra)-1 and letraAcert == False:
                chances -= 1
                print(f'Você errou a letra. Suas chances são: {chances}')
                print(palavraAcert)

        
        tentativas.append(tentativa)
            
        if palavraAcert == palavra:
            acertou = True
            print('Você acertou a palavra!')
            return True

        if chances == 0:
            print(f'Suas tentativas acabaram. A palavra era {palavra}')
            return False


forca(palavra)