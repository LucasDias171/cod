from time import sleep

def contador(inic, fim, passo):
    print(f'contagem de {inic} até {fim} pulando de {passo} em {passo}')
    sleep(1.5)
    if inic < fim:
        while inic <= fim:
            print(f'{inic} ', end='')
            sleep(0.5)
            inic += passo
        print('\nFIM')
    else:
        while inic >= fim:
            if passo == 0:
                passo = 1
            if passo < 0:
                passo *= -1
            print(f'{inic} ', end='')
            sleep(0.5)
            inic -= passo

        print('FIM')


#princ

contador(1, 220, 12)
contador(10, 0, -2)
i = int(input('Iínio: '))
f = int(input('Fim: '))
deslocamento = int(input('Passo: '))
contador(i, f, deslocamento)