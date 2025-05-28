#reto 

lista = [300, 5, 3, 7,0, 9, 200, -3, 76]

def ordenar():
    for izq in range (len(lista)-1):
        for der in range (izq +1, len (lista)):
            if lista [izq]< lista [der]:
                tem = lista[izq]
                lista [izq]= lista [der]
                lista [der]= tem 

        print (f"der: {lista}")
    print (f"izq:{lista}")

ordenar()
#investigar como funciona el quicksort