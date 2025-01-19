graphs={
        'A' : ['A'], 
        'B' : ['C','E','A'], 
        'C' : ['D'], 
        'D' : ['H'], 
        'E' : ['C'], 
        'F' : ['E'], 
        'G' : ['F'],
        'H' : ['A','G']
    }

def bfs(graph,start,end):
    queue = [start]
    visited = []
    current = ''
    neighbor = ''
    
    while queue:
        current = queue.pop(0)
        if current == end:
            visited.append(current)
            break
        if current not in visited:
            visited.append(current)
            neighbor = graph[current]
            for x in neighbor:
                queue.append(x)
    return print(visited)

nodeAwal = input("Masukkan node awal: ")
nodeTujuan = input("Masukkan node tujuan: ")
print("Jalur yang dilewati: " + str(bfs(graphs, nodeAwal, nodeTujuan)))