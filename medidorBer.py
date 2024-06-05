
def medidorBER(original, recibido):
    errorCount = 0
    print("original Len",len(original), "recibido len", len(recibido))
    if len(original) != len(recibido):
        return abs(len(original) - len(recibido))
    
    # Iterate over index
    for i in range(0, len(original)):
        if(original[i] != recibido[i]):
            errorCount += 1

    print(f"Numero de Errores : {errorCount}")
    print(f"BER : {errorCount/len(original)}")
    return errorCount