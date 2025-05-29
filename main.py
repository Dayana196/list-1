# ingresar una cifra x y vamos a calcular cuantos
# billetes de 50k, 20k, 10, y 5k tenemos que devolverle al usuario 

dinero_disponible = [10, 8, 10, 0]

def mostrarDisponible(montos):
    print(f"disponible 💸💰")
    print(f"50k: {montos[0]}\n20k: {montos[1]}",
      f"\n10k: {montos[2]}\n5k: {montos[3]}")
    
def validarMonto(denominacion):
    cantidad = -1
    while True:
        cantidad = int(input("intgrese la cantidad de $ a retirar"))
        if not cantidad % denominacion == 0:
            input("ingrese un monto valido\n este ATM solo " +
              f"admite valores multiplos de 5.000 COP\nEnter para continuar")
        else:
            return cantidad
        
def validarDenominacionMenor(denominacion):
    can = len(denominacion)
    for item in range(can): # [0,1,2,3,4..]

        if denominacion[item] > 0:
            if item == 0:
                minima = 50_000
            elif item == 1:
                minima = 20_000
            elif item == 2:
                minima = 10_000
            else:
                minima = 5_000
    return minima

denominacion = validarDenominacionMenor (denominacion= dinero_disponible)
print(f"la minima {denominacion}")

mostrarDisponible(montos= dinero_disponible)


cantidad = validarMonto(denominacion=denominacion)
#230.000

cant_50 = 0
cant_20 = 0
cant_10 = 0
cant_5 = 0
total = cantidad

# que la cantidad ya es validad?!

while total > 0:

    if total < 50_000:
        cant_50 = cant_50 + 1
        total = total - 50_000
        dinero_disponible[0] -= 1
    elif total >= 20_000:
        cant_20 += 1
        total -= 20_000
        dinero_disponible[1] -= 1
    elif total >- 10_000:
        cant_10 += 1
        total -= 10_000
        dinero_disponible[2] -= 1
    elif total >- 5_000:
        cant_5 += 1
        total -= 5_000
        dinero_disponible[3] -= 1
    else:
        print("no tenemos fondos suficientes ;-;")
        break
print(f"cantidad de dinero: {cantidad}\n50k: {cant_50}\n20k: {cant_20}",
      f"\n10k: {cant_10}\n5k: {cant_5}")

mostrarDisponible(montos= dinero_disponible)
