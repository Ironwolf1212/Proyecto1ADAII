from tkinter import *
from tkinter import filedialog
from openInput import formatInput
from fuerzaBruta import ordenOptimoFB
from Voraz import ordenOptimo
from Dinamica import ordenOptimoPD
import copy
from tkinter import messagebox
#from Dinamica import riegoOptimo

root = Tk()

root.title("Riego Optimo")

root.minsize(300, 200)
root.maxsize(1280, 720)

root.pack_propagate(False)

def abrirArchivo():
    filePath = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
    finca = formatInput(filePath)
    pintarFinca(finca)
    return finca

lbl = Label(root)
lbl.config(font=("Arial", 20))
lbl.grid()

btn = Button(root, text = "Abrir archivo", command = abrirArchivo)
btn.grid(column=0, row=1)
btn.config(font=("Arial", 20))

def home():
    lbl.configure(text="Seleccione un archivo de Entrada", justify="center")
    btn.grid(column=0, row=1)

def generarOutput(resultado, costo):
    with open("resultado.txt", "w") as f:
        #f.write("Costo: " + str(costo) + "\n")
        f.write(str(costo) + "\n")
        #f.write("Orden de riego Optimo:\n")
        for riego in resultado:
            f.write(str(riego) + "\n")

def calcularVoraz(finca, result_window):
    print("Finca de entrada: ",finca)
    resultado, costo = ordenOptimo(finca)
    print(resultado)
    result_lbl_1 = Label(result_window, text="Costo: " + str(costo))
    result_lbl_1.config(font=("Arial", 20))
    result_lbl_1.pack()
    result_lbl = Label(result_window, text="Orden de riego Optimo: " + str(resultado))    
    result_lbl.config(font=("Arial", 20))
    result_lbl.pack()
    result_lbl_2 = Label(result_window, text="Se ha guardado el resultado en el archivo 'resultado.txt'")  
    result_lbl_2.config(font=("Arial", 20))
    result_lbl_2.pack()
    generarOutput(resultado, costo)


def calcularFB(finca, result_window):
    print("Finca de entrada: ",finca)
    resultado, costo = ordenOptimoFB(finca)
    print(resultado)
    result_lbl_1 = Label(result_window, text="Costo: " + str(costo))
    result_lbl_1.config(font=("Arial", 20))
    result_lbl_1.pack()
    result_lbl = Label(result_window, text="Orden de riego Optimo: " + str(resultado))    
    result_lbl.config(font=("Arial", 20))
    result_lbl.pack()
    result_lbl_2 = Label(result_window, text="Se ha guardado el resultado en el archivo 'resultado.txt'")  
    result_lbl_2.config(font=("Arial", 20))
    result_lbl_2.pack()
    generarOutput(resultado, costo)

def calcularPD(finca, result_window):
    print("Finca de entrada: ",finca)
    resultado, costo = ordenOptimoPD(finca)
    print(resultado)
    result_lbl_1 = Label(result_window, text="Costo: " + str(costo))
    result_lbl_1.config(font=("Arial", 20))
    result_lbl_1.pack()
    result_lbl = Label(result_window, text="Orden de riego Optimo: " + str(resultado))    
    result_lbl.config(font=("Arial", 20))
    result_lbl.pack()
    result_lbl_2 = Label(result_window, text="Se ha guardado el resultado en el archivo 'resultado.txt'")  
    result_lbl_2.config(font=("Arial", 20))
    result_lbl_2.pack()
    generarOutput(resultado, costo)

def formatearTextoFinca(finca):
    texto = ""
    if len(finca) <= 10:
        for plantacion in finca:
            texto += str(plantacion) + "\n"
    else:
        for i in range(10):
            texto += str(finca[i]) + "\n"
        texto += "...\n"
    return texto

def pintarFinca(finca):
    lbl.configure(text = "Finca: " + "\n" + formatearTextoFinca(finca) + "\n" + "Seleccione un tipo de Programación" + "\n", justify="center")
    lbl.grid(columnspan=3)
    btn.grid_forget()

    btnFuerzaBruta = Button(root, text = "Fuerza Bruta", command=lambda: abrirVentanaResultadoFB(copy.copy(finca)))
    btnFuerzaBruta.config(font=("Arial", 20))
    btnFuerzaBruta.grid(column=0, row=2, padx=10, pady=10)

    btnVoraz = Button(root, text = "Voraz", command=lambda: abrirVentanaResultadoVoraz(copy.copy(finca)))
    btnVoraz.config(font=("Arial", 20))
    btnVoraz.grid(column=1, row=2, padx=10, pady=10)

    btnDinamica = Button(root, text = "Dinamica", command=lambda: abrirVentanaResultadoPD(copy.copy(finca)))
    btnDinamica.config(font=("Arial", 20))
    btnDinamica.grid(column=2, row=2, padx=10, pady=10)
    

def abrirVentanaResultadoVoraz(finca):
    result_window = Toplevel(root)
    result_window.title("Resultado Voraz")
    result_window.geometry("600x300")
    calcularVoraz(finca, result_window)

def abrirVentanaResultadoFB(finca):
    result_window = Toplevel(root)
    result_window.title("Resultado Fuerza Bruta")
    result_window.geometry("600x300")
    calcularFB(finca, result_window)

def abrirVentanaResultadoPD(finca):
    result_window = Toplevel(root)
    result_window.title("Resultado Fuerza Bruta")
    result_window.geometry("600x300")
    calcularPD(finca, result_window)

def Reiniciar():
    home()
    btn_reiniciar.grid_forget()

btn_reiniciar = Button(root, text = "Reiniciar", command = Reiniciar)

home()
root.mainloop()