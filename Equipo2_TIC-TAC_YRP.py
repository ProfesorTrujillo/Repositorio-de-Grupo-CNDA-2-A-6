import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time # Importo la librería necesaria para gestionar los tiempos 

# Se define la configuración global de las rutas disponibles en el sistema
# Se utiliza como base la información de los recorridos con origen en la Universidad Tecnológica de Aguascalientes
CONFIG_RUTAS = {
    "Ruta 50 ": {"paradas": 10, "tiempo_base": 8},
    "Ruta 50-B": {"paradas": 12, "tiempo_base": 7},
    "Ruta 41-penal": {"paradas": 15, "tiempo_base": 10},
    "Ruta 25": {"paradas": 8, "tiempo_base": 9}
}

def salir_sistema():
    """Cierra la aplicación por completo."""
    ventana.destroy()

def guardar_comentario():
    comentario = caja_comentarios.get("1.0", tk.END).strip()
    if comentario:
        messagebox.showinfo("Comentario Guardado", "Gracias por ayudar a brindar un mejor servicio")
        caja_comentarios.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Atención", "Por favor, escribe un comentario antes de guardar.")

def mostrar_soporte():
    lf_monitoreo.pack_forget()
    lf_acceso.pack_forget()
    lf_soporte.pack(fill="both", expand=True, padx=10, pady=10)

def mostrar_panel_control():
    lf_soporte.pack_forget()
    lf_acceso.pack(fill="x", padx=10, pady=5)
    lf_monitoreo.pack(fill="both", expand=True, padx=10, pady=5)

# Se define esta función para la validación del identificador de sesión del usuario
def validar_id_usuario(id_ingresado):
    # Se verifica que el dato cumpla con el formato global establecido para la activación de la sesión.
    if id_ingresado.isdigit() and len(id_ingresado) == 6:
        return True
    else:
        return False

def ejecutar_validacion():
    """Maneja la entrada del ID único del usuario."""
    id_id = entrada_id.get()
    if validar_id_usuario(id_id):
        lbl_tarjeta.config(text=f"SESIÓN ACTIVA: {id_id}", fg="#C8E6C9")
        btn_iniciar_ruta.config(state="normal")
        btn_entrar.config(state="disabled")
        entrada_id.config(state="disabled")
    else:
        messagebox.showerror("ID Inválido", "El ID de usuario debe ser de 6 dígitos numéricos.")

# Se define la lógica para el cálculo de aproximación de las paradas restantes
# Se utiliza una operación aritmética para determinar los minutos estimados de llegada a la siguiente parada
def calcular_aproximacion(parada_actual, total_paradas, minutos_base): 
    faltantes = total_paradas - parada_actual 
    tiempo_espera = faltantes * minutos_base 
      
    return faltantes, tiempo_espera 

# Se define este procedimiento para la sincronización del sistema con la plataforma de movilidad
def sincronizar_gps(segundos_pausa): 
    """ 
    Se utiliza para simular la comunicación constante con el servidor central de la CMOV.
    """ 
    # Se utiliza una pausa programada para reflejar el comportamiento del rastreo satelital en tiempo real
    time.sleep(segundos_pausa)

def iniciar_monitoreo():
    """Ejecuta el recorrido dinámico basado en la ruta elegida."""
    btn_iniciar_ruta.config(state="disabled")
    combo.config(state="disabled")
    
    ruta_seleccionada = combo.get()
    datos = CONFIG_RUTAS[ruta_seleccionada]
    total = datos["paradas"]
    base = datos["tiempo_base"]
    
    for p in range(1, total + 1):
        faltantes, tiempo = calcular_aproximacion(p, total, base)
        
        # Salida de datos en la interfaz
        lbl_camion.config(text=f"UBICACIÓN ACTUAL DEL CAMIÓN: PARADA {p}")
        
        if p < total:
            lbl_paradas.config(text=f"PARADAS RESTANTES A TERMINAL: {faltantes}")
            lbl_tiempo.config(text=f"TIEMPO DE APROXIMACIÓN: {tiempo} MINUTOS")
        else:
            lbl_paradas.config(text="¡HA LLEGADO A SU DESTINO!")
            lbl_tiempo.config(text="UNIDAD EN TERMINAL")
        
        ventana.update()
        sincronizar_gps(0.4) 

    messagebox.showinfo("Viaje Finalizado", f"Has llegado al final de la {ruta_seleccionada}.\n¿Deseas consultar otra ruta?")
    
    # Permitir al usuario cambiar de ruta al terminar
    combo.config(state="readonly")
    btn_iniciar_ruta.config(state="normal", text="Monitorear otra ruta")


ventana = tk.Tk()
ventana.title("GUI_Proyecto_TIC-TAC_YRP")
ventana.geometry("1000x650")
ventana.configure(bg="#9BB7CC")

color_header = "#2F4156"   
color_menu = "#567C8D"      
color_content = "#519FA1"   
color_accent = "#FFFFFF"    


encabezado = tk.Frame(ventana, bg=color_header, height=80)
encabezado.pack(fill="x")

titulo = tk.Label(encabezado, text="TIC-TAC RUTA", bg=color_header, 
                  fg=color_accent, font=("Segoe UI", 22, "bold"))
titulo.place(x=20, y=20)

subtitulo = tk.Label(encabezado, text="Coordinación General de Movilidad - Aguascalientes", 
                      bg=color_header, fg="#F5EFEB", font=("Segoe UI", 10, "italic"))
subtitulo.place(x=25, y=55)


menu = tk.Frame(ventana, bg=color_menu, width=200)
menu.pack(side="left", fill="y")

btn_inicio = tk.Button(menu, text="Panel de Control", bg=color_menu, fg="white", 
                        relief="flat", font=("Segoe UI", 11), command=mostrar_panel_control)
btn_inicio.pack(fill="x", pady=20, padx=10)

btn_ayuda = tk.Button(menu, text="Soporte Técnico", bg=color_menu, fg="white", 
                       relief="flat", font=("Segoe UI", 11), command=mostrar_soporte)
btn_ayuda.pack(fill="x", pady=10, padx=10)

btn_salir = tk.Button(menu, text="Salir del Sistema", bg="#D32F2F", fg="white", 
                       relief="flat", font=("Segoe UI", 11, "bold"), command=salir_sistema)
btn_salir.pack(side="bottom", fill="x", pady=20, padx=10)


contenido = tk.Frame(ventana, bg=color_content)
contenido.pack(side="left", fill="both", expand=True, padx=30, pady=30)


lf_acceso = tk.LabelFrame(contenido, text="", bg=color_content, borderwidth=0)
lf_acceso.pack(fill="x", padx=10, pady=5)

lbl_tarjeta = tk.Label(lf_acceso, text="Ingrese su ID de Usuario (6 dígitos):", bg=color_content, 
                       font=("Segoe UI", 11), fg=color_accent)
lbl_tarjeta.grid(row=0, column=0, padx=20, pady=20)

entrada_id = tk.Entry(lf_acceso, width=25, font=("Segoe UI", 11))
entrada_id.grid(row=0, column=1, padx=10)

btn_entrar = tk.Button(lf_acceso, text="Activar Sesión", bg=color_header, fg="white", 
                       font=("Segoe UI", 10, "bold"), command=ejecutar_validacion)
btn_entrar.grid(row=0, column=2, padx=20)

# 2. BLOQUE DE MONITOREO DINÁMICO
lf_monitoreo = tk.LabelFrame(contenido, text="", bg=color_content, borderwidth=0)
lf_monitoreo.pack(fill="both", expand=True, padx=10, pady=5)

lbl_sel = tk.Label(lf_monitoreo, text="Seleccionar Ruta:", bg=color_content, 
                   font=("Segoe UI", 11), fg=color_accent)
lbl_sel.place(x=30, y=10)

combo = ttk.Combobox(lf_monitoreo, values=list(CONFIG_RUTAS.keys()), state="readonly")
combo.current(0)
combo.place(x=160, y=12)

btn_iniciar_ruta = tk.Button(lf_monitoreo, text="Ver Ubicación en Tiempo Real", bg="#2F4156", fg="white",
                             font=("Segoe UI", 10, "bold"), state="disabled", command=iniciar_monitoreo)
btn_iniciar_ruta.place(x=350, y=8)

lbl_camion = tk.Label(lf_monitoreo, text="ESPERANDO ACTIVACIÓN DE SESIÓN...", 
                      bg="#C8DDE6", fg="#1B5A5E", font=("Segoe UI", 12, "bold"), width=60, pady=10)
lbl_camion.place(x=30, y=80)

lbl_paradas = tk.Label(lf_monitoreo, text="PARADAS RESTANTES: --", 
                       bg="#C4D2FF", fg="#179CF5", font=("Segoe UI", 12, "bold"), width=60, pady=10)
lbl_paradas.place(x=30, y=140)

lbl_tiempo = tk.Label(lf_monitoreo, text="TIEMPO ESTIMADO: --", 
                      bg="#BCDBFF", fg="#0CA4BF", font=("Segoe UI", 12, "bold"), width=60, pady=10)
lbl_tiempo.place(x=30, y=200)

# 3. BLOQUE DE SOPORTE Y QUEJAS
lf_soporte = tk.LabelFrame(contenido, text="", bg=color_content, borderwidth=0)

lbl_quejas = tk.Label(lf_soporte, text="ATENCIÓN CIUDADANA: 4491234567", 
                      bg=color_header, fg="white", font=("Segoe UI", 14, "bold"), pady=10)
lbl_quejas.pack(fill="x", pady=10)

caja_comentarios = tk.Text(lf_soporte, height=8, width=60, font=("Segoe UI", 10))
caja_comentarios.pack(pady=10)

frame_botones_soporte = tk.Frame(lf_soporte, bg=color_content)
frame_botones_soporte.pack(pady=10)

tk.Button(frame_botones_soporte, text="Enviar Sugerencia", bg="#4CAF50", fg="white", 
          font=("Segoe UI", 10, "bold"), command=guardar_comentario).pack(side="left", padx=10)
tk.Button(frame_botones_soporte, text="Cerrar Aplicación", bg="#D32F2F", fg="white", 
          font=("Segoe UI", 10, "bold"), command=salir_sistema).pack(side="left", padx=10)

ventana.mainloop()
