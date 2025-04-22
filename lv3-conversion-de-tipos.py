""" Declara una variable tipo string con valor "123", conviértela a número y realiza una operación matemática. """

numero_str: str = "123"

mi_numero: int = int(numero_str)

operacion_matematica: int = mi_numero - 23

print(f'El valor "{numero_str}" era un string, y ahora convertido a número es {mi_numero}. le reste 23 asi que ahora es {operacion_matematica}')