import tkinter as tk
from tkinter import ttk

# Ventana principal de nuestro programa con el nombre de nuestro equipo
#declaramos la variable ventana que es nuestro lienzo en blanco 
ventana = tk.Tk()
ventana.title("GUI_Proyecto_TIC-TAC_YRP")
#decalramos el tamaño de la ventana 
ventana.geometry("1000x600")
#elegimos colores beige por que son colores calidos que no molestan
ventana.configure(bg="#9BB7CC")  #se declaro el fondo de la ventana 

# Declaramos la paleta de colores a aplicar en la ventana 
color_header = "#2F4156"   
color_menu = "#567C8D"      
color_content = "#519FA1"   
color_accent = "#FFFFFF"    


# Se declara el primer frame principal de la ventana , en este se le pone la posicion y el color 
encabezado = tk.Frame(ventana, bg=color_header, height=80)
encabezado.pack(fill="x")

# Empezamos a poner nuestros widgets . asi empezando con la vista principal de nuestra ventana . poniendo como titulo nuestro nombre de proyecto 
titulo = tk.Label(encabezado, text="TIC-TAC RUTA", bg=color_header, 
                  fg=color_accent, font=("Segoe UI", 22, "bold"))
titulo.place(x=20, y=20)
#Declaramos la variable encabezado para poner un subtitulo para la empresa que le correspode el codigo 
subtitulo = tk.Label(encabezado, text="Coordinación General de Movilidad - Aguascalientes", 
                     bg=color_header, fg="#F5EFEB", font=("Segoe UI", 10, "italic"))
subtitulo.place(x=25, y=55)

#Declaramos el color del menu 
menu = tk.Frame(ventana, bg=color_menu, width=200)
menu.pack(side="left", fill="y")

# Declaramos las variables que se encontraran en el menu y que se podran presionar 
btn_inicio = tk.Button(menu, text="Panel de Control", bg=color_menu, fg="white", 
                       relief="flat", font=("Segoe UI", 11), activebackground=color_header)
btn_inicio.pack(fill="x", pady=20, padx=10)

btn_ayuda = tk.Button(menu, text="Soporte Técnico", bg=color_menu, fg="white", 
                      relief="flat", font=("Segoe UI", 11))
btn_ayuda.pack(fill="x", pady=10, padx=10)

#Declaramos el tamaño del area de contenido de la ventana 
contenido = tk.Frame(ventana, bg=color_content)
contenido.pack(side="left", fill="both", expand=True, padx=30, pady=30)

#se pone como etiqueta la verificacion del camion (Esto esta en duda ya que pensandolo en equipo presenta incosistencia en nuestra logia , lo checaremos)
lf_acceso = tk.LabelFrame(contenido, text="", bg=color_content, 
                          font=("Segoe UI", 12, "bold"), fg=color_accent, borderwidth=0)
lf_acceso.pack(fill="x", padx=10, pady=10)

lbl_tarjeta = tk.Label(lf_acceso, text="ID Tarjeta de Ruta:", bg=color_content, font=("Segoe UI", 11), fg=color_accent)
lbl_tarjeta.grid(row=0, column=0, padx=20, pady=30)

# Se declara la caja de texto para que ingresen el ID 
entrada_id = tk.Entry(lf_acceso, width=25, font=("Segoe UI", 11))
entrada_id.grid(row=0, column=1, padx=10)

# Se declara el boton para validar que la informacion es correcta (del ID)
btn_entrar = tk.Button(lf_acceso, text="Validar", bg=color_header, fg="white", font=("Segoe UI", 10, "bold"))
btn_entrar.grid(row=0, column=2, padx=20)


lf_monitoreo = tk.LabelFrame(contenido, text="", bg=color_content, 
                             font=("Segoe UI", 12, "bold"), fg=color_accent, borderwidth=0)
lf_monitoreo.pack(fill="both", expand=True, padx=10, pady=10)

# Se pone un boton selectivo que hara el trabajo de que el usuario pueda ingresar que ruta quiere saber su posicion 
lbl_sel = tk.Label(lf_monitoreo, text="Seleccionar Ruta:", bg=color_content, font=("Segoe UI", 11), fg=color_accent)
lbl_sel.place(x=30, y=30)
#Nos faltan rutas por poner pero por el ejemplo implementamos las rutas que salen de la UTA
combo = ttk.Combobox(lf_monitoreo, values=["Ruta 50 ", "Ruta 50-B", "Ruta 41-penal","Ruta 25"], state="readonly")
combo.current(0)
combo.place(x=160, y=32)

# Estructuramos los valores predominados que seran puestos por funciones , el usuario solo tiene la capacidad de verlos no de modificar esto 
lbl_camion = tk.Label(lf_monitoreo, text="UBICACIÓN ACTUAL DEL CAMIÓN:", 
                      bg="#C8DDE6", fg="#1B5A5E", font=("Segoe UI", 12, "bold"), width=60, pady=10)
lbl_camion.place(x=30, y=100)

lbl_paradas = tk.Label(lf_monitoreo, text="PARADAS RESTANTES PARA LLEGAR A LA TERMINAL:", 
                       bg="#C4D2FF", fg="#179CF5", font=("Segoe UI", 12, "bold"), width=60, pady=10)
lbl_paradas.place(x=30, y=160)

lbl_tiempo = tk.Label(lf_monitoreo, text="TIEMPO DE APROXIMACIÓN SIGUIENTE PARADA:", 
                      bg="#BCDBFF", fg="#0CA4BF", font=("Segoe UI", 12, "bold"), width=60, pady=10)
lbl_tiempo.place(x=30, y=220)
#Cerramos la ventana 
ventana.mainloop()
