#hacer una lista de utiles 


print("LISTA DE UTILES")

utiles = []
item = []
menu = """
·················································
:   ╔───────────────────────────────╗           :
:   │ _ __ ___    ___  _ __   _   _ │           :
:   │| '_ ` _ \  / _ \| '_ \ | | | |│           :
:   │| | | | | ||  __/| | | || |_| |│           :
:   │|_| |_| |_| \___||_| |_| \__,_|│           :
:   ╚───────────────────────────────╝           :
: 1. Listar los Utiles Inutiles                 :
: 2. Actualizar un Util Inutil                  :
: 3. Eliminar un Util Inutil                    :
: 4. Finalizar                                  :
·················································
"""

def Mostrarutiles(listadeutiles):
    print ("✏️ Lista de inutiles ")
    for util in listadeutiles: 
      print(f"Nombre: {util[0]} cantidad:{util[1]}")

while True:
   print (menu)
   opcion =int(input("selecciona una opcion del menu: \n"))
   if opcion ==1:
    nombre = input("Ingrese el nombre de util inutil: \n")
    cantidad = int(input(f"Ingrese la cantidad de {nombre}: \n"))
    item.append (nombre)
    item.append (cantidad)
    utiles.append (item.copy)
    print (utiles)
    item.clear()
   elif opcion==2: 
       Mostrarutiles (utiles)
   elif opcion ==3 :
      Mostrarutiles (utiles)
      itemNombre= input ("Ingresa el nombre del util inutil a buscar:\n ")
      print (utiles)
   for utilindex in range(len(utiles)):
      if utiles[utilindex][0]== itemNombre: 
            nuevonombre = input (f"ingrese el nuevo valor para{utiles[utilindex][0]}") 
            utiles[utilindex][0]=nuevonombre
      elif opcion == 5:
        break
      


