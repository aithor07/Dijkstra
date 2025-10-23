# Inicializamos un grafo no dirigido con pesos en las aristas
# Cada clave representa un nodo, y cada valor es una lista de tuplas (nodo_vecino, peso)
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target = ''):
    """
    Calcula las distancias mínimas desde un nodo de inicio 'start' hasta todos
    los demás nodos (o hasta uno específico 'target', si se indica).
    """

    # Lista de nodos aún no visitados
    unvisited = list(graph)

    # Diccionario que almacena las distancias mínimas conocidas desde 'start'
    # Al inicio, la distancia a start es 0, y al resto es infinita
    distances = {node: 0 if node == start else float('inf') for node in graph}

    # Diccionario que guarda los caminos más cortos hasta cada nodo
    # Inicialmente todos los caminos están vacíos
    paths = {node: [] for node in graph}
    paths[start].append(start)  # El camino al nodo de inicio es él mismo
    
    # Bucle principal: se ejecuta mientras queden nodos sin visitar
    while unvisited:
        # Se elige el nodo no visitado con la distancia más corta conocida
        current = min(unvisited, key=distances.get)

        # Recorremos los vecinos del nodo actual
        for node, distance in graph[current]:
            # Si la distancia al vecino a través del nodo actual es menor que la conocida...
            if distance + distances[current] < distances[node]:
                # Actualizamos la distancia más corta a ese vecino
                distances[node] = distance + distances[current]

                # Actualizamos el camino más corto hacia ese nodo
                if paths[node] and paths[node][-1] == node:
                    # Si ya tenía un camino con el mismo nodo final, lo reemplazamos
                    paths[node] = paths[current][:]
                else:
                    # Si no, añadimos la ruta del nodo actual
                    paths[node].extend(paths[current])
                # Añadimos el nodo final al camino
                paths[node].append(node)

        # Marcamos el nodo actual como visitado
        unvisited.remove(current)
    
    # Si se indicó un nodo objetivo, solo se muestra ese resultado
    # De lo contrario, se imprimen todos los caminos desde el nodo inicial
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue  # No tiene sentido mostrar el camino desde start hasta él mismo
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    # Devolvemos las estructuras con las distancias y los caminos más cortos
    return distances, paths
    
# Llamada al algoritmo: buscamos los caminos mínimos desde A a todos los demás nodos
shortest_path(my_graph, 'A')
