mensaje = "hola"
mensaje += " "
mensaje += "Ernesto"
print(mensaje)

print("Concatenación:")

mensaje = "hola"
espacio = " "
nombre = "Ernesto"
print(mensaje + espacio + nombre)

numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("el resultado de la suma es: " + resultado)

print("Busqueda:")

mensaje = "Hola Ernesto"
buscar_subcadena = mensaje.find("Ernesto")
print(buscar_subcadena)

print("Extraccion")

mensaje = "Hola Ernesto"
extraer_cadena =  mensaje[1:8]
print(extraer_cadena)

print("comparación:")

mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)