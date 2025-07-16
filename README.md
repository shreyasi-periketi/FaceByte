# FaceByte
Social Graph Search

## Project Overview
This project simulates how a social media app like FaceByte can use classic AI search algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), and A* to trace user connections on a social network graph. Each user is a node, and friendship or interaction links between users form edges with weights representing either connection strength or similarity. The goalis to find friend paths and suggest new connections by analyzing the shortest or most "diverse" paths between users.

## Features Implemented
### 1. breadth_first_search(start, end, graph)
Finds the shortest path (by number of hops) between users. Ideal for “Find Friends” functionality.
- Uses connection-only time maps
- Implements tree search, avoids cycles
- Explores level by level (friend → friend-of-friend, etc.)

### 2. depth_first_search(start, end, graph)
Finds a path (not guaranteed to be shortest) using a depth-first strategy. Explores paths deeply before backtracking.
- Also supports the “Find Friends” feature
- Does not track visited nodes (as per assignment rules)
- Suitable for graphs without loops

### 3. a_star_search(start, end, graph, heuristic)
Finds the most “dissimilar” path with minimum total similarity points, using A* with a heuristic.
- Powers the “Suggested Friends” feature
- Uses:
  - Time Map → cost so far (g(n))
  - Distance Map → heuristic estimate (h(n))
- Implements a graph search: avoids re-expanding visited nodes
- Handles tie-breaking using heuristic + order of insertion

## The Goal
The goal is to prototype intelligent friend-suggestion and tracing systems based on social connection graphs. The aim was to evaluate and compare different pathfinding algorithms for:
1. Tracing mutual connections
2. Suggesting diverse new friends
3. Handling both weighted and unweighted graphs

## Task Rules & Constraints
- DFS: Can re-expand nodes on different branches. No visited list.
- BFS: Must maintain a visited list to avoid loops.
- A*: Must use expand() function from expand.py. Avoid revisiting nodes (graph search).





