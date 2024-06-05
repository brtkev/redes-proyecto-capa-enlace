
POLIGONO12 = [1,1,1,0,1,0,0,0,1,0,0,1,1]

# POLIGONO31 = [1,1,0,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,1,1,0,1,1,1]

# libro de redes => x32 + x26 + x23 + x22 + x16 + x12 + x11 + x10 + x8 + x7 + x5 + x4 + x2 + x1 + 1
POLIGONO32 = [1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1]

def codificar(msg : str, divisor : list[int]) -> str:
    longitudCRC = len(divisor) - 1
    
    datos = [int(char) for char in msg]

    for i in range(longitudCRC): datos.append(0)

    cociente, residuo = dividirUsandoXOR(datos, divisor)

    # verificar si hubo error
    error = existeUnBit(residuo)
    
    # si no hubo el CRC es todos 0, 
    # no se si esto pueda suceder, pero aqui esta la validacion igual
    if not error: return "".join([str(bit) for bit in datos])

    # si hubo error, que es lo normal, estonces el CRC es el residuo
    resultado = [int(char) for char in msg]
    resultado.extend(residuo)
    return "".join([str(bit) for bit in resultado])

def decodificar(msg : str, divisor : list[int]) -> tuple[str, bool]:
    datos = [int(bit) for bit in msg]

    cociente, residuo = dividirUsandoXOR(datos, divisor)

    error = existeUnBit(residuo)

    mensajeSinCRC = msg[:len(msg) - len(divisor) + 1]

    return mensajeSinCRC, error


def existeUnBit( bits : list[int]) -> bool:
    # verificar si hubo error
    for bit in bits: 
        if bit != 0: 
            return True
        
    return False

def dividirUsandoXOR( dividendo : list[int], divisor : list[int]) -> tuple[list[int], list[int]]:
    
    lDivisor = len(divisor)

    if( len(dividendo) < len(divisor)) : return IndexError("el dividendo no puede ser mas pequeño que el divisor")

    cociente = []
    residuo = []
    for bit in dividendo:
        residuo.append(bit)

        # primeros bits
        if len(residuo) < lDivisor:
            continue

        # validacion de cociente 0
        if residuo[0] == 0:
            residuo.pop(0)
            cociente.append(0)
            continue

        cociente.append(1)

        residuo = XORBits(residuo, divisor)

        residuo.pop(0)

    return cociente, residuo


def XORBits( a : list[int], b : list[int]) -> list[int] | None:
    if len(a) != len(b) : return

    result = []
    for i in range(len(a)):
        result.append(a[i] ^ b[i])
    return result




if __name__ == "__main__":

    msg = "11010101010"#100010011110010101"
    a12 = codificar(msg, POLIGONO12)
    a32 = codificar(msg, POLIGONO32)

    print(a12)
    #1101010101010110011111
    a12 = "1011010100010110111111"
    print(a32)

    print(decodificar(a12, POLIGONO12))
    print(decodificar(a32, POLIGONO32))
    #11010101010
    
    # print(len(DIVISOR))

    # dividendo = [1,0,0,1,0,0,0,0,0]
    # divisor = [1,1,0,1]

    # print(dividirUsandoXOR(dividendo, divisor))

    # div = [1, 1, 1, 0, 0, 0, 0, 0, 1]

    # print(dividirUsandoXOR(div, divisor))

    # ejem = [1,1,1,0,0,1,0,1,0,1]
    # a = ejem.copy()
    # b = ejem.copy()
    # a.extend([0,0,0])

    # print(dividirUsandoXOR(a, divisor))

    # b.extend([1, 1, 0])
    # print(dividirUsandoXOR(b, divisor))


    
    # residuo = [1, 0, 0, 0]
    
    # print(XORBits(divisor, residuo))

    
