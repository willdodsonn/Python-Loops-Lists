# `12.1` More mapping

El m茅todo `map()` de una lista, llama a una funci贸n por cada valor en la lista y, luego, entrega una nueva lista con los valores modificados.

```py
#incrementando en 1
def values_list(number) {
  return number + 1
}

my_list = [1, 2, 3, 4]
result = map(values_list, my_list)  #retorna [2, 3, 4, 5]
```

## 馃摑 Instrucciones:

1. Crear una funci贸n llamada `increment_by_one` que multiplicar谩 cada n煤mero por 3.

2. Pasa un argumento a la funci贸n.

3. Usa la funci贸n `map()` de la lista para ejecutar la funci贸n `increment_by_one` a trav茅s de cada valor en la lista.

4. Almacena la nueva lista en una nueva llamada `new_list` e imprime los nuevos valores.

## 馃挕 Pista:

+ La funci贸n coger谩 un par谩metro con el elemento original y lo transformar谩 e insertar谩 en una nueva lista (`new_list`).

+ Recuerda que tu funci贸n debe devolver cada nuevo elemento para almacenarlo en la nueva lista (`new_list`).


