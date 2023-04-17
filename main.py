import tkinter as tk
from tkinter import ttk


def main():
    def seleccion(evento):
        seleccionado = listaElementos[cajaLista.curselection()[0]]
        if seleccionado not in listaSeleccionados:
            listaSeleccionados.append(seleccionado)
            elementos = ', '.join([str(elementos) for elementos in listaSeleccionados])
            label.config(text=f'Vas a querer: {elementos}')
            print(elementos)

    def reiniciar():
        listaSeleccionados.clear()
        label.config(text='Vas a querer:')

    def salir():
        print(listaSeleccionados)
        root.quit()

    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    pedido = tk.Label(root, text='Como vas a querer tu hamburgesa?')
    pedido.grid(column=0, row=0, padx=10, pady=10)

    listaElementos = ['Queso', 'Lechuga', 'Tomate', 'Pepinillos', 'Aderezos']
    lista = tk.StringVar(value=listaElementos)
    listaSeleccionados = []
    elementos = ""
    cajaLista = tk.Listbox(root, height=10, listvariable=lista)
    cajaLista.grid(column=0, row=1, pady=10, padx=10)
    cajaLista.bind("<<ListboxSelect>>", seleccion)

    label = tk.Label(root, text='Vas a querer:')
    label.grid(column=0, row=2, padx=10, pady=10)

    boton = tk.Button(root, text='Reiniciar', command=reiniciar)
    boton.grid(column=0, row=3, padx=10, pady=10)

    salir = tk.Button(root, text='Listo', command=salir)
    salir.grid(column=0, row=4, padx=10, pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()
