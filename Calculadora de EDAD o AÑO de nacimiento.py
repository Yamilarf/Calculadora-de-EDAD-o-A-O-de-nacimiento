"""calculadora de año de nacimiento o edad"""
 

import tkinter as tk

# Operacion para obtener el resultado que deseamos
def restar():
    num1 = float(CajaTexto2.get())#".get"lleva los valores para que al presionar el boton nos arroje un resultado
    num2 = float(CajaTexto1.get())
    resultado = num1 - num2
    CajaTexto3.delete(0, tk.END)
    CajaTexto3.insert(0, resultado)

# titulo, tamaño, y color de la ventana
ventana= tk.Tk()
ventana.geometry("600x300")
ventana.title ("CALCULA EN QUE AÑO QUE NACIO TU ABUELO/A O CUANTOS VA A CUMPLIR")
ventana.configure(bg="yellow")

#etiqueta asignada a la primera caja de texto
etiqueta=tk.Label( ventana,text= "Nombre:")
etiqueta.pack()
CajaTexto=tk.Entry(ventana)#caja de texto
CajaTexto.pack()
etiqueta.configure(bg="yellow")#color etiqueta

#etiqueta asignada a la segunda caja de texto
etiqueta=tk.Label( ventana,text= "AÑO de nacimiento o EDAD que cumplira este año:")
etiqueta.pack()
CajaTexto1=tk.Entry(ventana)#caja de texto
CajaTexto1.pack()
etiqueta.configure(bg="yellow")#color etiqueta1

#etiqueta asignada a la tercer caja de texto
etiqueta=tk.Label(ventana, text= "Año actual:")
etiqueta.pack()
CajaTexto2=tk.Entry(ventana)#caja de texto
CajaTexto2.pack()
etiqueta.configure(bg="yellow")#color etiqueta2

#boton y etiqueta en el mismo
boton = tk.Button(ventana, text="Calcular", command=restar)#permite traer el resultado de la operasion utilizada
boton.pack()
boton.configure(bg="orange")#color boton

#etiqueta de la ultima caja de texto
etiqueta=tk.Label(ventana,text= "El AÑO que nació tu Abu, o su EDAD es:")
etiqueta.pack()
CajaTexto3=tk.Entry(ventana)#caja de texto
CajaTexto3.pack()
etiqueta.configure(bg="yellow")#color etiqueta


ventana.mainloop()
