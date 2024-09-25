from tkinter import *

def entrada(texto_label, frame, inicio_x = 10, inicio_y = 10, ancho = 120, altura = 25):
    label = Label(frame, text=texto_label)
    label.place(x=inicio_x, y=inicio_y, width=ancho, height=altura)

    text = Entry(frame)
    text.place(x=inicio_x + ancho, y=inicio_y, width=ancho, height=altura)

def entradasMultiples(lista, frame, inicio_x = 10, inicio_y = 10, ancho = 120, altura = 25):
    for i in range (0,len(lista)):
        entrada(lista[i], frame, inicio_x, inicio_y, ancho, altura)
        inicio_y = inicio_y + altura + 3
    return inicio_y + altura + 3


ventana = Tk()
ventana.geometry("1200x680")

local = Frame(ventana, bg="blue", height = 600,width = 340)
local.place(x = 10, y = 10)

visitante = Frame(ventana, bg="red", height = 600,width = 340)
visitante.place(x = 360, y = 10)

partido = Frame(ventana, bg="grey", height = 600,width = 340)
partido.place(x = 710, y = 10)

ingreso = Frame(ventana, bg="black", height = 50, width=1040)
ingreso.place(x = 10, y = 610)



labels_local = ["Local", "Arquero", "Titular 2","Titular 3","Titular 4","Titular 5","Titular 6","Titular 7","Titular 8","Titular 9","Titular 10",
"Titular 11", "DT.", "Goles", "Amonestados", "Expulsados", "Cambios", "Penales a favor"]
entradasMultiples(labels_local, local)

labels_visitante = ["Visitante", "Arquero", "Titular 2","Titular 3","Titular 4","Titular 5","Titular 6","Titular 7","Titular 8","Titular 9","Titular 10",
"Titular 11", "DT.", "Goles","Amonestados", "Expulsados", "Cambios", "Penales a favor"]
entradasMultiples(labels_visitante, visitante)

labels_partido = ["Date", "Campeonato", "Temporada", "Fecha", "Local", "Internacional","Instancia", "Ida", "Vuelta", "Único", "Estadio", "Árbitro", "Recaudación", "Espectadores", "Suspendido", "Minuto"]
entradasMultiples(labels_partido, partido)

boton = Button(ingreso, text="Ingresar")
boton.place(x = 10, y = 10)




ventana.title("Recolección de datos")

ventana.mainloop()

'''
¿Qué falta?
- Checkbox en algunos: Suspendido, Ida/Vuelta/Unico, Local/Internacional, en seccion Goles (Pierna Izq/Derecha, Dentro/Fuera del area, Cabeza/Pie/Lo que sea, Penal), etc.
- Lista desplegable: en Goles (solo los jugadores de ese equipo o el otro), Cambios, Penales (como se atajo o erro), etc.
- Solapas: en la primera, equipo local, segunda, equipo visitante, tercera, partido.
- Sobreescribir bien en la base de datos de Excel. Las funciones ya creo que están.
- Opción partidos suspendidos: otra vez los 11 titulares más el técnico. Cuantos tiempos de cuantos minutos. Estadio. Fecha. Etc.

- Otra ventana con los planteles de cada temporada de cada equipo. Jugadores, técnicos (especificando renuncia, despido o lo que sea y la fecha), con sus datos:
nacionalidades, provincia y localidad, pie izquierdo o derecho, posición, dorsal, fecha de nacimiento, compras/Préstamos que vinieron y si al final o en el medio se vendio, 
siguio, rescindio, fue a prestamo o se retiro. 

- Otra ventana con las ubicaciones de los estadios y datos referentes a este.

'''