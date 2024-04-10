# Función para multiplicación
def Calcular(Numero1, Numero2, Numero3):
    PrimerResultado = Numero1 * Numero2 + Numero3
    return PrimerResultado

# Función para poder introducir los números
def Principal():
    Entrada1 = 5
    Entrada2 = 3
    Entrada3 = 7
    SegundoResutado = Calcular(Entrada1, Entrada2, Entrada3)
    print("El resultado es:", SegundoResutado)

Principal()
