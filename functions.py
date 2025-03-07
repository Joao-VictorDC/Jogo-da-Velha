matriz = [
    [0, 0, 0], 
    [0, 0, 0],
    [0, 0, 0]
    ]

def repetir(turno):
    turno = not turno
    return turno

def marcar(matriz, turno, x, y):
    for i in range(len(matriz)):
        if x == i:
            for j in range(3):
                if y == j:
                    if turno:
                        matriz[i][j] = 'X'
                    else:
                        matriz[i][j] = 'O'
                else:
                    pass
        else:
            pass

def condicao(matriz, turno):
    # Vitória na diagonal principal
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != 0:
        if turno:
            print("VITÓRIA DO X")
            exit()
        else:
            print("VITÓRIA DO O")
            exit()

    # Vitória na diagonal secundária
    if matriz[0][2] == matriz[1][1] == matriz[2][0] != 0:
        if turno:
            print("VITÓRIA DO X")
            exit()
        else:
            print("VITÓRIA DO O")
            exit()   

    for j in range(3):
        if matriz[0][j] == matriz[1][j] == matriz[2][j] != 0:
            if turno:
                print("VITÓRIA DO X")
                exit()
            else:
                print("VITÓRIA DO O")
                exit()   

    for i in matriz:
        if i.count('X') == 3:
            print("VITÓRIA DO X")
            exit()
        elif i.count('O') == 3:
            print("VITÓRIA DO O")
            exit()
        


 