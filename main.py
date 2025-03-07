from functions import *

matriz = [
    [0, 0, 0], 
    [0, 0, 0],
    [0, 0, 0]
    ]

play = 'S'
turno = False
vazios = 9

print(matriz)
while play == 'S':
    turno = not turno
    if turno:
        print("É a vez do X")
    else:
        print("É a vez do O")

    x = int(input("pos x: "))
    y = int(input("pos y: "))

    if not (matriz[x][y] == 'X' or matriz[x][y] == 'O'):
        marcar(matriz, turno, x, y)
        vazios -= 1
    else:
        print("Local já marcado!")
        turno = repetir(turno)

    for linha in matriz:
        for coluna in linha:
            print(f'{coluna}', end=' '),
        print("\n")


    if vazios == 0:
        print("Empate")
        exit()
        
    condicao(matriz, turno)
