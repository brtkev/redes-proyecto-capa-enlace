
def agregaBitsDeRelleno(mensaje : str) -> str:
    mensajeConRellenoDeBits = ""
    unosSeguidos = 0
    for i in range(len(mensaje)):
        currBit = mensaje[i]

        mensajeConRellenoDeBits += currBit

        # 5 unos seguidos inserta un bit 0 de relleno
        if currBit == "1":
            unosSeguidos += 1
            if unosSeguidos == 5:
                mensajeConRellenoDeBits += '0'
                unosSeguidos = 0
        else:
            unosSeguidos = 0

    return mensajeConRellenoDeBits

def eliminarBitsDeRelleno(mensaje : str) -> str:
    mensajeSinRellenoDeBits = ""
    unosSeguidos = 0
    
    for i in range(len(mensaje)):
        currBit = mensaje[i]

        if unosSeguidos == 5 and currBit == '0':
            unosSeguidos = 0
        else:
            mensajeSinRellenoDeBits += currBit

        if currBit == "1":
            unosSeguidos += 1
        else:
            unosSeguidos = 0

    return mensajeSinRellenoDeBits



def __testRellenoDeBits(mensaje : str) -> None:
    print(f"mensaje original : '{mensaje}'")

    mensajeConRellenoDeBits = agregaBitsDeRelleno(mensaje)
    print(f"mensaje con relleno de bits : '{mensajeConRellenoDeBits}'")

    mensajeSinRellenoDeBits = eliminarBitsDeRelleno(mensajeConRellenoDeBits)
    print(f"mensaje sin relleno de bits : '{mensajeSinRellenoDeBits}'")

    print(f"mensaje original y mensaje sin relleno son iguales ? {mensajeSinRellenoDeBits == mensaje}")


if __name__ == '__main__':
    __testRellenoDeBits('011011111111111111110010')
    