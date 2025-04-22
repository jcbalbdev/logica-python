""" Declara una constante para el valor de PI y úsala para calcular el área de un círculo con radio 4. muestra solo dos decimales """

PI: float = 3.141592
RADIO_CIRCULO: int = 4

area_circulo: float = PI*RADIO_CIRCULO**2

print(f"el radio del circulo es {RADIO_CIRCULO} y su area es {area_circulo:.2f}")

