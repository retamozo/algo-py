def bubble_sort(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            print(lista[j])
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        # el primer minimo index por default es i.
        # O sea, en la primera pasada va a ser 0.
        min_index=i
        # Lo mismo con el valor minimo.
        min_value=arr[min_index]
        # itero de nuevo, pero a partir del valor de i para
        # irme corriendo siempre al subarray de la izquierda
        # ejemplo [ 2,5,9,1]
        # en la primera pasada, el dos queda como el valor minimo y su indice 0 como
        # el minimo index. En la segunda pasada, i vale 1, por lo tanto su valur es 5. Y asi
        # sucecivamente
        for j in range(i, len(arr) - 1):
            # Si valor actual (i) es mayor al siguiente (j + 1). Si 2 es mas grande que 5
            if min_value > arr[j + 1]:
                min_value= arr[j + 1]
                min_index = j + 1
        # este swap es necesario para mantener sincronizadas las pasadas.
        if min_index != i:
            aux = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = aux
    return arr


# la lista tiene que estar ordenada
def busqueda_binaria(lista, elemento):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = izq + (der - izq) // 2
        if lista[medio] == elemento:
            return medio
        if lista[medio] < elemento:
            izq = medio + 1
        else:
            der = medio - 1
    return -1

lista = [2, 10, 55, 87, 90]
print(busqueda_binaria(lista, 87))


