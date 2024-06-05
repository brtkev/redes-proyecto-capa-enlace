
from functools import reduce

def obtenerPosicionesParidad(msg : list | str) -> list[int]: 
    posicionesPariedad = [ ]
    j = 0
    for i in range(1, len(msg)):
        if i == 2**j :
            posicionesPariedad.append(i-1)
            j+=1
    return posicionesPariedad
    
def validarHamming( hamming : list[int]) -> int:
    # validar hamming inicial
    indices = [i+1 for i, bit in enumerate(hamming) if bit]
    if not indices: return 0
    return reduce(lambda x, y: x ^ y, indices)


def codificarHamming( msg : str) -> str:
    hamming = datosAHamming(msg)

    # validar hamming inicial
    result = validarHamming(hamming)

    # si es valido, retorna
    if result == 0: return "".join([str(c) for c in hamming])
    
    #si no, obtiene las posiciones de los bits de paridad (1,2,4,8,etc)
    posicionesPariedad = obtenerPosicionesParidad(hamming)

    #valida cada bit de paridad
    for index in posicionesPariedad:
        parity = 0
        for j in range(len(hamming)):
            # validamos todas las posiciones (j) que tienen el bit de paridad (index)
            if j+1 & index+1 == index+1:
                parity = parity ^ hamming[j]
            
        # guardamos la paridad calculada
        hamming[index] = parity

    return "".join([str(c) for c in hamming])

def datosAHamming( datos : str | list) -> list[int]:
    hamming = []
    # crear hamming inicial
    i = j = k = 0
    while i < len(datos):
        if k & 2**j - 1 != 2**j - 1  :
            hamming.append(int(datos[i]))
            i+=1
        else:
            hamming.append(0)
            j+=1

        k+=1

    return hamming


def decodificarHamming( msg : str) -> tuple[str, int]:
    bits = [int(c) for c in msg]

    # validamos la paridad del mensaje
    result = validarHamming(bits)

    # si encontramos 1 error, lo podemos arreglar
    if result != 0: bits[result-1] = 0 if bits[result-1] else 1

    # transformamos de hamming a datos originales
    res = hammingADatos(bits)

    return res, result

def hammingADatos(hamming : str | list ) -> str:
    # transformamos de hamming a datos originales
    res = ""
    j=0
    for i in range(len(hamming)) : 
        if i != 2**j - 1: 
            res += str(hamming[i])
        else:
            j+=1
    return res


def codificarHammingExtended(msg : str) -> str:
    hamming = codificarHamming(msg)

    paridad = 0
    for c in hamming:
        if c == '1': paridad = paridad ^ 1

    return str(paridad) + hamming

def decodificarHammingExtended(msg : str) -> tuple[str, int, bool]:
    
    hamming = msg[1:]
    paridad = 0
    for c in hamming:
        if c == '1': paridad = paridad ^ 1

    errorExtended = True
    if paridad == int(msg[0]): errorExtended = False

    datos, error = decodificarHamming(hamming)
    return datos, error, errorExtended

if __name__ == '__main__':
    # Enter the data to be transmitted
    #version 1
    data = '1011001'

    ham = codificarHamming(data)
    print("agregarHamming function", ham)

    bits = [int(c) for c in ham]
    i = 6
    bits[i] = 0 if bits[i] else 1
    ham = "".join([str(c) for c in bits])

    res = decodificarHamming(ham)
    print("errorCorrection function", res)
    


