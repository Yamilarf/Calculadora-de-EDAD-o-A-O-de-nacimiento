"""calculadora de año de nacimiento o edad"""
 

import tkinter as tk

def restar():
    num1 = float(CajaTexto2.get())
    num2 = float(CajaTexto1.get())
    resultado = num1 - num2
    CajaTexto3.delete(0, tk.END)
    CajaTexto3.insert(0, resultado)


ventana= tk.Tk()
ventana.geometry("600x300")
ventana.title ("CALCULA EN QUE AÑO NACIO TU ABUELO/A O CUANTOS VA A CUMPLIR")
ventana.configure(bg="yellow")

etiqueta=tk.Label( ventana,text= "Nombre:")
etiqueta.pack()
CajaTexto=tk.Entry(ventana)
CajaTexto.pack()
etiqueta.configure(bg="yellow")

etiqueta=tk.Label( ventana,text= "AÑO de nacimiento o EDAD que cumplira este año:")
etiqueta.pack()
CajaTexto1=tk.Entry(ventana)
CajaTexto1.pack()
etiqueta.configure(bg="yellow")

etiqueta=tk.Label(ventana, text= "Año actual:")
etiqueta.pack()
CajaTexto2=tk.Entry(ventana)
CajaTexto2.pack()
etiqueta.configure(bg="yellow")

boton = tk.Button(ventana, text="Calcular", command=restar)
boton.pack()
boton.configure(bg="orange")

etiqueta=tk.Label(ventana,text= "El AÑO que nació tu Abu, o su EDAD es:")
etiqueta.pack()
CajaTexto3=tk.Entry(ventana)
CajaTexto3.pack()
etiqueta.configure(bg="yellow")


ventana.mainloop()