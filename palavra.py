palavra_secreta = 'PATO'
acertou = False
errou = False

while not acertou and not errou:


    def captura_palavra():
        letra = input('Digite uma letra: ').upper()
        while len(letra) > 1:
            print('Digite apenas uma letra.')
            break
        return letra

    resposta = captura_palavra()
    print(resposta)

    