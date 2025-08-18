

treinta = 30
cuarenta_y_cinco = 45
cincuenta = 50
sesenta_y_tres = 63



#Implementa una función anónima que reciba un número entero por parámetro 
# (por ejemplo, la variable trinta) y retorne True si el número es mayor a 50. 
# Guarda la función (sin ejecutar) en una variable llamada mayor_a_cincuenta.

#Esta función debe retornar un valor booleano (True o False).




# your code here
mayor_a_cincuenta = lambda trinta: trinta > 50




## AUTO-CALIFICADOR

# Base variables
treinta = 30
cuarenta_y_cinco = 45
cincuenta = 50
sesenta_y_tres = 63
    
# Caso 1: no existe la función.
try:
    mayor_a_cincuenta
    assert type(mayor_a_cincuenta) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada mayor_a_cincuenta.")

# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    mayor_a_cincuenta(treinta)
    mayor_a_cincuenta(cuarenta_y_cinco)
    mayor_a_cincuenta(cincuenta)
    mayor_a_cincuenta(sesenta_y_tres)
except:
    raise RuntimeError("Tu función produce un error al ejecutarse.")
    
# Caso 3: la función no es de tipo lambda
assert str(mayor_a_cincuenta).find("lambda") > -1, "Tu función no es anónima o de tipo lambda."

# Caso 4: la función retorna un valor no booleano
assert type(mayor_a_cincuenta(sesenta_y_tres)) == bool, f"Tu función debe retornar un valor de tipo {bool.__name__}."

# Caso 5: condición contraria (num < 50)
assert mayor_a_cincuenta(sesenta_y_tres) and not mayor_a_cincuenta(treinta), "La condición de tu función es incorrecta. Es probable que tengas que utilizar un símbolo de desigualdad contrario."

# Caso 6: usa mayor o igual
assert not mayor_a_cincuenta(cincuenta), "50 no es mayor a 50."

# Caso 7: diversos casos
try:
    assert not mayor_a_cincuenta(treinta)
    assert not mayor_a_cincuenta(cuarenta_y_cinco)
    assert not mayor_a_cincuenta(cincuenta)
    assert mayor_a_cincuenta(sesenta_y_tres)
except AssertionError as e:
    e.args += ("Tu función no retorna el booleano correcto.",)
    raise e
    
# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")