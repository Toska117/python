

lista = [23, "2", 46 , "l", 8.3, "m"]



# your code here

def primera_letra(lista):
    for elemento in lista:
        if isinstance(elemento, str) and elemento.isalpha():
            return elemento
    return ""


#Implementa una función llamada primera_letra que reciba una lista de números y letras por parámetro
#  (por ejemplo, la variable lista), y retorne el primer elemento que sea una letra. 
# La función debe retornar una cadena de texto vacía ("") si no encuentra una letra.
#Esta función debe retornar una letra.



## AUTO-CALIFICADOR

# Base variables
lista = [23, "2", 46 , "l", 8.3, "m"]
lista_prueba = [23.7, "15", "22.2", 21, 48, "x", 24, 15.9, "f"]
lista_prueba_2 = [23.7, "15", "22.2", 21, "x", 24, 15.9, "f"]
lista_prueba_3 = [23.7, "15", "22.2", 21, 24, 15.9]

# Caso 1: no existe la función.
try:
    primera_letra
    assert type(primera_letra) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada primera_letra.",)
    
# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    primera_letra(lista)
    primera_letra(lista_prueba)
    primera_letra(lista_prueba_2)
    primera_letra(lista_prueba_3)
except:
    raise RuntimeError("Tu función produce un error al ejecutarse.")
    
# Caso 3: no retorna una letra
assert type(primera_letra(lista_prueba)) == str, f"Tu función debe retornar un valor de tipo {str.__name__}."

# Caso 4: respuesta explicita
assert primera_letra(lista_prueba) != "l", "Tu respuesta es incorrecta para para una instancia diferente. Utiliza el parámetro."

# Caso 5: la función retorna vacio
assert primera_letra(lista_prueba_3) == "", "Tu función debe retornar una cadena de texto vacía cuando no hay una letra en la lista."

# Caso 6: no encuentra letras.
assert primera_letra(lista_prueba) != "", "Tu función no encuentra una letra en la lista. Puede no estar explorando todos sus elementos."

# Caso 7: retorna una letra distinta de la esperada
assert primera_letra(lista_prueba) == "x", "Tu función no retorna la letra correcta."
assert primera_letra(lista) == "l", "Tu función no retorna la letra correcta."

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")

