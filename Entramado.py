import RellenoDeBits, ParidadDeBits, Hamming, CRC
from typing import Literal

SEPARADOR = "01111110"
TRAMA_SIZE = 11
TRAMA_SIZE_CRC = 64 
OPCION_LITERAL = Literal["", "paridad", "hamming", "hammingExtended", "CRC12", "CRC32"]

def entramar( mensaje : str, opcion :  OPCION_LITERAL = "", par = True ) -> str:
    
    mensajeEntramado = SEPARADOR
    salto = TRAMA_SIZE
    if opcion == "CRC12" or opcion == "CRC32": salto = TRAMA_SIZE_CRC
 
    for i in range(0, len(mensaje), salto):        
        bits = mensaje[i:i+salto]

        if opcion == "paridad":
            bits = ParidadDeBits.agregarBitDeParidad(bits, par)
        
        elif opcion == "hamming":
            bits = Hamming.codificarHamming(bits)

        elif opcion == "hammingExtended":
            bits = Hamming.codificarHammingExtended(bits)

        elif opcion == "CRC12" : 
            bits = CRC.codificar(bits, CRC.POLIGONO12)

        elif opcion == "CRC32" : 
            bits = CRC.codificar(bits, CRC.POLIGONO32)

        bits = RellenoDeBits.agregaBitsDeRelleno(bits)
        mensajeEntramado += bits + SEPARADOR

    return mensajeEntramado

def desentramar( mensaje : str, opcion :  OPCION_LITERAL = "", par = True) -> tuple[str, int]:
    errorCount = 0
    mensajeDesentramado = ""

    listaDeTramas = mensaje.split(SEPARADOR)

    for i in range(len(listaDeTramas)):
        if listaDeTramas[i] == '': continue
        currTrama = listaDeTramas[i]
        bits = RellenoDeBits.eliminarBitsDeRelleno(currTrama)

        if opcion == "paridad":
            bits, error = ParidadDeBits.eliminarBitDeParidad(bits, par)
            if( error == 1): errorCount += 1

        elif opcion == "hamming":
            bits, errorIndex = Hamming.decodificarHamming(bits)
            if( errorIndex != 0 ): errorCount += 1
            
        elif opcion == "hammingExtended":
            bits, errorIndex, errorExtended = Hamming.decodificarHammingExtended(bits)
            if( not errorExtended and errorIndex != 0 ) : errorCount += 2
            elif( errorExtended ): errorCount += 1

        elif opcion == "CRC12" : 
            bits, error = CRC.decodificar(bits, CRC.POLIGONO12)
            if error: errorCount += 1 

        elif opcion == "CRC32" : 
            bits, error = CRC.decodificar(bits, CRC.POLIGONO32)
            if error: errorCount += 1
        

        mensajeDesentramado += bits

    return mensajeDesentramado, errorCount
    



if __name__ == '__main__':
    mensaje = "011011111111111111110010"
    mensajeEntramado = entramar(mensaje)

    mensajeDesentramado, error = desentramar(mensajeEntramado)

    print(f"mensaje              : {mensaje}")
    print(f"mensaje desentramado : {mensajeDesentramado} | error : {error}")
    print(f"mensaje original es igual a mensaje desentramado ? {mensaje == mensajeDesentramado}")