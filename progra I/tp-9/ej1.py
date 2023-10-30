import random
from sort import selection_sort;





def maximo(lista):
     for i in range(len(lista)):
        if i == 0 or lista[i] > max:
            pos = i
            max = lista[i]
     print(f"El elemento maximo es {max} y esta en la posicion {pos}")

def busqueda_lineal(lista, valorBuscado):
    pos=-1
    i=0
    while pos==-1 and i < len(lista):
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos

#  Crear una lista de N numeros generados al azar entre 0 y 100
#  pero sin elementos repetidos

def ejercicio1():
    lista = []
    cantidad_numeros = int(input("Ingrese un numero menor o igual que 100 \n"))
    while(cantidad_numeros > 100):
        cantidad_numeros = int(input("Ingrese un numero menor o igual que 100 \n"))

    while len(lista) < cantidad_numeros:
        nro_random = random.randint(0, 100)
        if busqueda_lineal(lista, nro_random) == -1:
            lista.append(nro_random)
    # esto es muy choto. La posta es la solucion de arriba
    # for _ in range(cantidad_numeros):
    #     nro_random = random.randint(0, 100)
    #     print(nro_random)
    #     while (busqueda_lineal(lista, nro_random) == -1):
    #        lista.append(nro_random)
    print(lista)


# Se dispone de 5 nums distintos (enteros).
# Se pide:
#     - Guardar los 5 nros en un vector
#     - integresar un nro entero
#     - Indicar en que posicion se encuentra ese nro
def ejercicio_dos():
    lista = []
    for _ in range(5):
        nro_random = random.randint(0, 100)
        lista.append(nro_random)
    print(f"Lista generada {lista}")
    nro = int(input("Ingrese el numero a buscar \n"))
    posicion = busqueda_lineal(lista, nro);
    if  posicion != -1:
        print(f"El elemento {nro} esta en la posición {posicion}")
    else:
        print(f"El elemento {nro} no existe en la lista")


# def cargaInicial(ll,ln):


def multiple_max(lista):
    if not lista:
         raise ValueError("Debe proporcionar una lista")
    maximos=[]
    indices_max=[]
    for i in range(len(lista)):
        if(i == 0 or lista[i] > current_max):
            current_max = lista[i]
            maximos.append(current_max)
            indices_max.append(i)
    return maximos, indices_max


def encontrar_maximos(lista):
    if not lista:
        return []  # Devolver una lista vacía si la lista de entrada está vacía

    maximos = [lista[0]]  # Inicializar la lista de máximos con el primer elemento
    max_indices = [0]  # Inicializar la lista de índices de máximos con 0

    for i in range(1, len(lista)):
        if lista[i] > maximos[0]:
            maximos = [lista[i]]
            max_indices = [i]
        elif lista[i] == maximos[0]:
            maximos.append(lista[i])
            max_indices.append(i)

    return maximos, max_indices

# Ejemplo de uso
mi_lista = [3, 2, 5, 5, 1, 6, 5]
maximos, indices = encontrar_maximos(mi_lista)

print("Máximos encontrados:", maximos)
print("Índices de los máximos:", indices)

#     auxLegajo=int(input("Ingrese un legajo"))
#     while auxLegajo<=0 and auxLegajo !=-1:
#         auxLegajo=int(input("Ingrese un legajo"))

#     while auxLegajo !=-1:

#         pos=busqueda(ll, auxLegajo)
#         if pos==-1:
#             nota=random.randint(1,10)
#             ll.append(auxLegajo)
#             ln.append(nota)
#         else:
#             print("LEGAJO DUPLICADO")

#         auxLegajo=int(input("Ingrese un legajo"))
#         while auxLegajo<=0 and auxLegajo !=-1:
#             auxLegajo=int(input("Ingrese un legajo"))



# def ordenamiento (ll,ln):
#      for i in range(len(ll)-1):
#          for j in range(len(ll)-1-i):
#              if ll[j]>ll[j+1]:
#                  aux=ll[j]
#                  ll[j]=ll[j+1]
#                  ll[j+1]=aux

#                  aux=ln[j]
#                  ln[j]=ln[j+1]
#                  ln[j+1]=aux



# def listado(ll,ln):
#     print(" ------- LISTADO DE LEGAJOS Y NOTAS -------")

#     for i in range(len(lc)):
#         print(ll[i],"\t",ln[i])





# # aqui comienza el principal
# LEGAJOS=[]
# NOTAS=[]

# cargaInicial(LEGAJOS,NOTAS)

# print(LEGAJOS)
# print(NOTAS)

# if len(NOTAS)>0:
#     aprobados=0
#     desaprobados=0
#     suma=0

#     for i in range(len(NOTAS)):

#         if NOTAS[i]>=4:
#             aprobados+=1
#         else:
#             desaprobados+=1

#         suma+=NOTAS[i]

#     print("La cantidad de aprobados ", aprobados)
#     print("La cantidad de desaprobados ",desaprobados)

#     promedio=suma/len(NOTAS)

#     print("La nota promedio es ", promedio)

#     for i in range(len(NOTAS)):
#         if NOTAS[i]>promedio:
#             print("Legajo que supera el promedio ",LEGAJOS[i])

#     ordenamiento(LEGAJOS,NOTAS)
#     listado(LEGAJOS,NOTAS)

# else:
#     print("NO SE INGRESARON DATOS")



