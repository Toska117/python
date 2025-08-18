

lista = [4, 3, 8, 5, 6, 2, 7, 5]

#Implementa una función llamada separar_pares_impares que reciba una lista de números enteros por
#  parámetro (por ejemplo, la variable lista) y retorne una tupla que contenga dos listas, cada una ordenada ascendentemente:

#    La primera lista debe contener los números pares.
#   La segunda lista debe contener los números impares.

#Esta función debe retornar una tupla de listas.



# your code here
def separar_pares_impares(lista):
    pares = sorted([num for num in lista if num % 2 == 0])
    impares = sorted([num for num in lista if num % 2 != 0])
    return (pares, impares)




# Base variables
lista = [4, 3, 8, 5, 6, 2, 7, 5]
lista_prueba = [3, 1, 2, 8, 6, 6, 7, 10, 9, 8]

# Caso 1: no existe la función.
try:
    separar_pares_impares
    assert type(separar_pares_impares) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada separar_pares_impares.")

# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    separar_pares_impares(lista)
    separar_pares_impares(lista_prueba)
except:
    raise RuntimeError("Tu función produce un error al ejecutarse.")

# Caso 3: no retorna una tupla de listas
assert type(separar_pares_impares(lista_prueba)) == tuple, f"Tu función debe retornar un valor de tipo {tuple.__name__}."
assert type(separar_pares_impares(lista_prueba)[0]) == list and type(separar_pares_impares(lista_prueba)[1]) == list, "La tupla que retorna tu función debe contener una lista en su primera y segunda posicion."

# Case 4: len(tupla) != 2
assert len(separar_pares_impares(lista_prueba)) == len(([],[])), "Tu función retorna una tupla de tamaño incorrecto."

# Caso 5: respuesta explicita
assert separar_pares_impares(lista_prueba) == ([2, 6, 6, 8, 8, 10], [1, 3, 7, 9]), "Tu respuesta es incorrecta para para una instancia diferente. Utiliza el parámetro."

# Caso 6: la lista de impares está ubicada antes que la lista de pares.
assert sum([i % 2 for i in separar_pares_impares(lista_prueba)[0]]) == 0, "La primera lista de la tupla debe contener únicamente pares."
assert sum([(i + 1) % 2 for i in separar_pares_impares(lista_prueba)[1]]) == 0, "La segunda lista de la tupla debe contener únicamente impares."

# Caso 7: la lista de pares y la lista de impares es cada una de longitud incorrecta
assert len(separar_pares_impares(lista_prueba)[0]) == len([2, 6, 6, 8, 8, 10]), "La primera lista de la tupla que retorna tu función no tiene la longitud correcta."
assert len(separar_pares_impares(lista_prueba)[1]) == len([1, 3, 7, 9]), "La segunda lista de la tupla que retorna tu función no tiene la longitud correcta."

# Caso 8: las listas son correctas, independiente de su orden
assert set(separar_pares_impares(lista_prueba)[0]) == {2, 6, 6, 8, 8, 10}, "La primera lista de la tupla que retorna tu función no contiene los elementos esperados, independiente de su orden."
assert set(separar_pares_impares(lista_prueba)[1]) == {1, 3, 7, 9}, "La segunda lista de la tupla que retorna tu función no contiene los elementos esperados, independiente de su orden."

# Caso 9: las listas no están ordenadas ascendentemente
assert separar_pares_impares(lista_prueba)[0] == [2, 6, 6, 8, 8, 10], "La primera lista de la tupla que retorna tu función no está ordenada ascendentemente."
assert separar_pares_impares(lista_prueba)[1] == [1, 3, 7, 9], "La segunda lista de la tupla que retorna tu función no está ordenada ascendentemente."

assert separar_pares_impares(lista)[0] == [2, 4, 6 ,8], "La primera lista de la tupla que retorna tu función no está ordenada ascendentemente."
assert separar_pares_impares(lista)[1] == [3, 5, 5, 7], "La segunda lista de la tupla que retorna tu función no está ordenada ascendentemente."

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")