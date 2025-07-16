from expand import expand
import heapq

def a_star_search(dis_map, time_map, start, end):
    
    def heuristic(node):
        return dis_map[node][end] if dis_map[node][end] is not None else float('inf')
    
    g = [(0, start)]
    visited = set()
    f_value = {v: float('inf') for v in time_map.keys()}
    f_value[start] = 0
    came_from = {}
    
    while g:
        _, current_node = heapq.heappop(g)
        if current_node == end:
            path = [current_node]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.insert(0, current_node)
            return path
        
        visited.add(current_node)
        
        for a in expand(current_node, time_map):
            tm_cost = time_map[current_node][a]
            if a in visited or tm_cost is None:
                continue
            
            cost = f_value[current_node] + tm_cost
            if cost < f_value[a]:
                f_value[a] = cost
                came_from[a] = current_node
                total_cost = cost + heuristic(a)
                temp = False
                for i, (priority, node) in enumerate(g):
                    if node == a:
                        temp = True
                        if total_cost < priority:
                            g[i] = (total_cost, a)
                            heapq.heapify(g)
                        break
                if not temp:
                    heapq.heappush(g, (total_cost, a))
    
    return None

def depth_first_search(time_map, start, end):
	stack = []  # DFS - stack
	# visited = set()  
	stack.append([start])
	
	while stack:
		path = stack.pop()
		node = path[-1]
		
		if node == end:
			return path
			
		# if node not in visited:
		neighbors = expand(node, time_map)
		for neighbor in neighbors:
			new_path = list(path)
			new_path.append(neighbor)
			stack.append(new_path)
		# visited.add(node)
			
	return []
	pass


def breadth_first_search(time_map, start, end):
	queue = [] # BFS - queue
	visited = set() # visited nodes
	queue.append([start])  # append starting node
	
	while queue:
		path = queue.pop(0)  # pop the starting node (for path)
		node = path[-1]  # last node from the path
		
		if node == end: # for when current node is destination, else next statement
			return path
		
		if node not in visited:
			neighbors = expand(node, time_map)  # For BFS, node's neighbors are needed
			for neighbor in neighbors:  # new path for neighbours
				new_path = list(path)
				new_path.append(neighbor)
				queue.append(new_path)
			visited.add(node)
			
	return []  # If no path is found (returns empty list)
