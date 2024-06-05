import tkinter
import tkinter.scrolledtext
import tkinter.ttk

import medidorBer
import Entramado


file = open("mensaje.txt", "r")
FILE_CONTENT = file.read()
file.close()

ventana = tkinter.Tk()
ventana.geometry("600x600")

etiqueta = tkinter.Label(ventana, text="Detector de Errores")

resultado = tkinter.StringVar() 
resultadoLabel = tkinter.Label(ventana, textvariable=resultado)


textArea = tkinter.scrolledtext.ScrolledText(ventana)

def trimMensaje(mensaje : str) -> str:
    mensajeTrimmed = ""
    for char in mensaje:
        if char == '1' or char == '0': mensajeTrimmed += char

    return mensajeTrimmed


def enviarMensaje():
    opcion = cmb.get()
    mensaje = trimMensaje(textArea.get("1.0", tkinter.END))
    errores = -1
    print("metodo: "+ opcion)
    if opcion == options[0]:
        errores = medidorBer.medidorBER(FILE_CONTENT, mensaje)

    elif opcion == options[1]:
        mensajeDesentramado, errores = Entramado.desentramar(mensaje, "paridad")
        
        error = medidorBer.medidorBER(FILE_CONTENT, mensajeDesentramado)
        print(f"medidor de ber : {error}")
    
    elif opcion == options[2]:
        mensajeDesentramado, errores = Entramado.desentramar(mensaje, "paridad", par=False)

    elif opcion == options[3]:
        mensajeDesentramado, errores = Entramado.desentramar(mensaje, "hamming")

    elif opcion == options[4]:
        mensajeDesentramado, errores = Entramado.desentramar(mensaje, "hammingExtended")

    elif opcion == options[5]:
        mensajeDesentramado, errores = Entramado.desentramar(mensaje, "CRC12")

    elif opcion == options[6]:
        mensajeDesentramado, errores = Entramado.desentramar(mensaje, "CRC32")

    print(f"errores : {errores}")
    resultado.set(f"errores : {errores}")


def cmbChange(event):
    opcion = cmb.get()
    mensaje = ""

    print(opcion)
    textArea.delete("1.0", tkinter.END)
    if opcion == options[0]:
        mensaje = FILE_CONTENT

    elif opcion == options[1]:
        mensaje = Entramado.entramar(FILE_CONTENT, "paridad")
    
    elif opcion == options[2]:
        mensaje = Entramado.entramar(FILE_CONTENT, "paridad", par=False)

    elif opcion == options[3]:
        mensaje = Entramado.entramar(FILE_CONTENT, "hamming")

    elif opcion == options[4]:
        mensaje = Entramado.entramar(FILE_CONTENT, "hammingExtended")

    elif opcion == options[5]:
        mensaje = Entramado.entramar(FILE_CONTENT, "CRC12")

    elif opcion == options[6]:
        mensaje = Entramado.entramar(FILE_CONTENT, "CRC32")

    textArea.insert("1.0", mensaje)
    resultado.set("")
        


boton = tkinter.Button(ventana, text="go!", padx=20, pady=10, command=enviarMensaje)

# Dropdown menu options 
options = [ 
    "nada", 
    "Paridad de Bits - Par", 
    "Paridad de Bits - Impar", 
    "Hamming Matricial", 
    "Hamming Matricial Extendido", 
    "CRC 12", 
    "CRC 32"
] 
  
# datatype of menu text 
clicked = tkinter.StringVar() 
  
# initial menu text 
clicked.set( "nada" ) 

cmb = tkinter.ttk.Combobox(ventana, values=options, textvariable=clicked)
cmb.bind("<<ComboboxSelected>>", cmbChange)

textArea.insert('1.0', FILE_CONTENT)


etiqueta.pack(side=tkinter.TOP)
cmb.pack()
textArea.pack(padx=20, pady=20)
boton.pack()
resultadoLabel.pack()

ventana.mainloop()