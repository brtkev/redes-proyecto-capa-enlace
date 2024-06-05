


def agregarBitDeParidad( mensaje : str, par = True ) -> str :
    """
    mensaje es la trama que a la que se agregara el bit de pariedad

    par es el tipo de pariedad, si es verdadero, entonces sera pariedad PAR sino IMPAR
    """
    bitPariedad = obtenerBitDePariedad(mensaje, par)

    return bitPariedad + mensaje

def eliminarBitDeParidad( mensaje : str, par = True ) -> tuple[str, int] :
    """
    mensaje es la trama que a la que se agregara el bit de pariedad

    par es el tipo de pariedad, si es verdadero, entonces sera pariedad PAR sino IMPAR
    """
    tramaSinParidad = mensaje[1:len(mensaje)]
    bitDePariedad = mensaje[0]
    bitDePariedadCalculado = obtenerBitDePariedad(tramaSinParidad, par)
    # print("    ", bitDePariedad, bitDePariedadCalculado)

    errores = 0
    if bitDePariedad != bitDePariedadCalculado:
        errores = 1
    
    return tramaSinParidad, errores

def obtenerBitDePariedad( mensaje : str, par = True) -> str:
    """
    mensaje es la trama que a la que se agregara el bit de pariedad

    par es el tipo de pariedad, si es verdadero, entonces sera pariedad PAR sino IMPAR
    """
    count1s = 0
    for i in range(0 ,len(mensaje)):
        currBit = mensaje[i]

        if currBit == '1':
            count1s += 1

    bitPariedad = '1' if par else '0'
    if count1s % 2 == 0:
        bitPariedad = '0' if par else '1'

    return bitPariedad


if __name__ == "__main__":
    trama = "0001111"
    tramaConBit = agregarBitDeParidad(trama)

    #error
    listTrama = list(tramaConBit)

    listTrama[3] = '1' if listTrama[3] == '0' else '0'

    tramaConBit = "".join(listTrama)
    #error

    tramaSinBit, errores = eliminarBitDeParidad(tramaConBit)

    print(f"trama : {trama}")
    print(f"trama con bit: {tramaConBit}")
    print(f"trama sin bit: {tramaSinBit}")
    print(f"error : {errores}")
    print(f"es trama original igual a trama sin bit ? {trama == tramaSinBit}")