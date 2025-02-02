from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

cities = [
    'Київ', 'Харків', 'Львів', 'Одеса', 'Дніпро', 'Запоріжжя', 'Вінниця', 'Тернопіль', 'Полтава', 'Чернігів'
]

G.add_nodes_from(cities)

edges = [
    ('Київ', 'Чернігів'),
    ('Київ', 'Полтава'),
    ('Київ', 'Вінниця'),
    ('Харків', 'Полтава'),
    ('Львів', 'Тернопіль'),
    ('Одеса', 'Вінниця'),
    ('Дніпро', 'Запоріжжя'),
    ('Дніпро', 'Полтава'),
    ('Запоріжжя', 'Полтава'),
    ('Вінниця', 'Тернопіль'),
    ('Полтава', 'Чернігів')
]

G.add_edges_from(edges)


plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=12, font_weight='bold', edge_color='gray')
plt.title('Граф обласних центрів України')
plt.show()


def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    path.append(start)
    visited.add(start)
    
    if start == goal:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path.copy(), visited)
            if result:
                return result
    return None


def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    
    while queue:
        (vertex, path) = queue.popleft()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph.neighbors(vertex):
                queue.append((neighbor, path + [neighbor]))
    return None

start_city = 'Київ'
goal_city = 'Запоріжжя'

path_dfs = dfs(G, start_city, goal_city)
path_bfs = bfs(G, start_city, goal_city)

print(f"Шлях DFS від {start_city} до {goal_city}: {path_dfs}")
print(f"Шлях BFS від {start_city} до {goal_city}: {path_bfs}")

weighted_edges = [
    ('Київ', 'Чернігів', 150),
    ('Київ', 'Полтава', 340),
    ('Київ', 'Вінниця', 270),
    ('Харків', 'Полтава', 140),
    ('Львів', 'Тернопіль', 130),
    ('Одеса', 'Вінниця', 430),
    ('Дніпро', 'Запоріжжя', 85),
    ('Дніпро', 'Полтава', 210),
    ('Запоріжжя', 'Полтава', 280),
    ('Вінниця', 'Тернопіль', 220),
    ('Полтава', 'Чернігів', 300)
]

G_weighted = nx.Graph()
G_weighted.add_weighted_edges_from(weighted_edges)

shortest_path = nx.dijkstra_path(G_weighted, start_city, goal_city)
shortest_path_length = nx.dijkstra_path_length(G_weighted, start_city, goal_city)

print(f"Найкоротший шлях від {start_city} до {goal_city} (Дейкстра): {shortest_path}")
print(f"Довжина найкоротшого шляху: {shortest_path_length} км")
