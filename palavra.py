
palavra_secreta = 'banana'
acertou = False
errou = False
# criando lista usando o for comprehension.
lista = ['_' for item in range(0, len(palavra_secreta))]

def entrada():
    # Capturando dados do usuario.
    letra = input('Digite uma letra: ').lower()
    while len(letra) > 1:
        print('Digite apenas uma letra por vez.')
        break
    return letra



while (not acertou and not errou):

    
    
    letra = entrada() # Chamando função
    # percorrendo lista e guardando as letra acertadas.
    index = 0
    for i in palavra_secreta:
        if(letra == i):
            lista[index] = letra
        index += 1    
    print(lista)    