from tkinter import *
from tkinter import filedialog
from openInput import formatInput
from fuerzaBruta import calcular_riego_optimo
from Voraz import ordenOptimo
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

def calcularVoraz(finca, result_window):
    resultado = ordenOptimo(finca)
    print(resultado)
    result_lbl = Label(result_window, text="Orden de riego Optimo: " + str(resultado))    
    result_lbl.config(font=("Arial", 20))
    result_lbl.pack()

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

    btnFuerzaBruta = Button(root, text = "Fuerza Bruta")
    btnFuerzaBruta.config(font=("Arial", 20))
    btnFuerzaBruta.grid(column=0, row=2, padx=10, pady=10)

    btnVoraz = Button(root, text = "Voraz", command=lambda: abrirVentanaResultado(finca))
    btnVoraz.config(font=("Arial", 20))
    btnVoraz.grid(column=1, row=2, padx=10, pady=10)

    btnDinamica = Button(root, text = "Dinamica")
    btnDinamica.config(font=("Arial", 20))
    btnDinamica.grid(column=2, row=2, padx=10, pady=10)
    

def abrirVentanaResultado(finca):
    result_window = Toplevel(root)
    result_window.title("Resultado Voraz")
    result_window.geometry("600x300")
    calcularVoraz(finca, result_window)

def Reiniciar():
    home()
    btn_reiniciar.grid_forget()

btn_reiniciar = Button(root, text = "Reiniciar", command = Reiniciar)

home()
root.mainloop()