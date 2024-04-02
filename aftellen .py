def dijkstra(graph, start):
    # Initialize distances as infinity and set distance to start node as 0
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Priority queue to hold nodes to be processed
    pq = deque()
    pq.append( (0, start) )
    
    while pq:
        current_distance, current_vertex = pq.popleft()
        # Do magic

    return distances

# Example graph
graph = {
      'A': {'B': 1, 'C': 4},
      'B': {'A': 1, 'C': 2, 'D': 5},
      'C': {'A': 4, 'B': 2, 'D': 1},
      'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))  
