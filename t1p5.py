lista = [3, 4, 2, 5, 5, 6, 3]

# Implementa una función llamada modulo_del_minimo que reciba una lista de números
#  enteros por parámetro (por ejemplo, la variable lista), encuentre el valor más pequeño que
#  se repita en la lista (min_val_rep) y retorne una función anónima. Esta función anónima debe 
# recibir un número entero mayor a cero (entero) por parámetro y retornar el residuo de la división 
# entre min_val_rep y entero (recomendamos usar el operador de residuo %).

#Esta función debe retornar una función anónima.
#Ejemplo

#    anon = modulo_del_minimo([3, 4, 2, 5, 5, 6, 3])
    
#    anon(2) == 1

#Una vez implementada la función modulo_del_minimo, ejectar el código anterior en una celda de Jupyter debe generar el output True.




# your code here
def modulo_del_minimo(lista):
    rep = {}
    for num in lista:
        rep[num] = rep.get(num, 0) + 1
    repetidos = [num for num in rep if rep[num] > 1]
    min_val_rep = min(repetidos) if repetidos else min(lista)
    return lambda entero: min_val_rep % entero



## AUTO-CALIFICADOR

# Base variables:
lista = [3, 4, 2, 5, 5, 6, 3]
lista_prueba = [6, 7, 4, 5, 8, 12, 15, 15, 8]

# Caso 1: no existe la función.
try:
    modulo_del_minimo
    assert type(modulo_del_minimo) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada modulo_del_minimo.")

# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    modulo_del_minimo(lista)
    modulo_del_minimo(lista_prueba)
except:
    raise RuntimeError("Tu función produce un error al ejecutarse.")
    
# Caso 3: la función no retorna una función anónima
try:
    assert type(modulo_del_minimo(lista_prueba)) == type(lambda:None)
    assert str(modulo_del_minimo(lista_prueba)).find("lambda") > -1
except:
    raise TypeError("Tu función debe retornar una función anónima (de tipo lambda).")
    
# Caso 4: la función anónima retornada es interrumpida por errores durante su ejecución.
try:
    for i in range(100):
        modulo_del_minimo(lista)(i + 1)
        modulo_del_minimo(lista_prueba)(i + 1)
except:
    raise RuntimeError("Se produce un error al ejecutar la función anónima que retorna tu función.")
    
# Caso 5: la función anónima retornada retorna algo distinto de un entero.
assert type(modulo_del_minimo(lista_prueba)(7)) == int, f"La función anónima que retorna tu función debería retornar un valor de tipo {type(0)}."
    
# Caso 6: el sentido del cálculo del residuo es incorrecto.
try:
    assert modulo_del_minimo(lista_prueba)(0) != 0
except AssertionError as e:
    raise ArithmeticError("La función anónima que retorna tu función calcula el residuo de la división de manera incorrecta. Prueba cambiar el orden de los elementos alrededor del operador '%'",)
except ZeroDivisionError as e:
    pass
    
# Caso 7: no identifica el menor elemento que se repite correctamente.
try:
    assert modulo_del_minimo(lista)(float("inf")) == 3
    assert modulo_del_minimo(lista_prueba)(float("inf")) == 8
except AssertionError as e:
    e.args += ("La función anónima que retorna tu función utiliza un valor inesperado en lugar del mínimo valor repetido en la lista.",)
    raise e
    
# Caso 8: diversos casos
try:
    assert modulo_del_minimo(lista_prueba)(4) == 0
    assert modulo_del_minimo(lista_prueba)(5) == 3
    assert modulo_del_minimo(lista_prueba)(8) == 0
    assert modulo_del_minimo(lista_prueba)(15) == 8
    assert modulo_del_minimo(lista)(3) == 0
    assert modulo_del_minimo(lista)(5) == 3
except AssertionError as e:
    e.args += ("Tu función retorna una función anónima incorrecta.",)
    raise e
    
# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")