pilhaOrigem = [3, 2, 1]
pilhaAuxiliar = []
pilhaDestino = []

def checaMovimento(origem, destino, disco):
    if destino == 1:
        if len(pilhaOrigem) == 0:
            return True
        if disco < pilhaOrigem[-1]:
            return True
    if destino == 2:
        if len(pilhaAuxiliar) == 0:
            return True
        if disco < pilhaAuxiliar[-1]:
            return True
    if destino == 3:
        if len(pilhaDestino) == 0:
            return True
        if disco < pilhaDestino[-1]:
            return True
    return False

while 1:
    print(pilhaOrigem)
    print(pilhaAuxiliar)
    print(pilhaDestino)
    if len(pilhaDestino) == 3:
        print("fim de jogo!")
        break
    print("digite de qual torre vc quer mover: (1,2,3) ")
    origem = int(input())
    if (origem not in [1, 2, 3]):
        print("torre inválida")
        break
    print("digite para qual torre vc quer mover: (1,2,3) ")
    destino = int(input())
    if (destino not in [1, 2, 3]):
        print("torre inválida")
        break
    if origem == 1:
        disco = pilhaOrigem[-1]
        pilhaOrigem.remove(disco)
    elif origem == 2:
        disco = pilhaAuxiliar[-1]
        pilhaAuxiliar.remove(disco)
    elif origem == 3:
        disco = pilhaDestino[-1]
        pilhaDestino.remove(disco)

    if checaMovimento(origem, destino, disco):
        if destino == 1:
            pilhaOrigem.append(disco)
        elif destino == 2:
            pilhaAuxiliar.append(disco)
        elif destino == 3:
            pilhaDestino.append(disco)
    else:
        print("movimento inválido")
        break
