
palavra_secreta = 'rato'
numero_tentativas = len(palavra_secreta) + 2

# criando lista usando o for comprehension.
lista = ['_' for item in range(0, len(palavra_secreta))]

def entrada():
    # Capturando dados do usuario.
    letra = input('Digite uma letra: ').lower()
    while len(letra) > 1:
        print('Digite apenas uma letra por vez.')
        break
    return letra



while (True):

    
    # percorrendo lista e guardando as letra
    letra = entrada() # Chamando função
    
    index = 0
    for i in palavra_secreta:
        if(letra == i):
            lista[index] = letra
        index += 1    
    print(lista) 
    print(f'Faltam {numero_tentativas} chances.')
    numero_tentativas -= 1 
    if '_' not in lista or numero_tentativas == 0:
        print('Fim do Jogo.')
        break
    

    
   
