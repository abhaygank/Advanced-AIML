import time
from collections import deque
W, H = 5, 5
obstacles = {(1, 1), (2, 4), (3, 4)} 
tasks = {(0, 2), (2, 1), (3, 0)} 
agent = (0, 0) 

# BFS to find shortest path
def bfs(s, g):
    # Holds (current_pos, path_so_far)
    q = deque([(s, [s])])

    # Set of visited nodes
    seen = {s}
    while q:
        (x, y), path = q.popleft()

        # If goal reached return path
        if (x, y) == g:
            return path

        # Explore 4 possible moves
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy  # New position

            # Check if inside grid, not an obstacle, and not visited
            if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in obstacles and (nx, ny) not in seen:
                q.append(((nx, ny), path + [(nx, ny)]))
                seen.add((nx, ny))  # Mark as visited
    return None


# Function to print the grid
def show():
    print("\n".join(" ".join(
        "A" if (x, y) == agent else
        "T" if (x, y) in tasks else
        "X" if (x, y) in obstacles else
        "."
        for y in range(H))
        for x in range(W)))
    print()
    
    # Pause so movement can be observed
    time.sleep(0.5)

# Show initial board
print("Initial Board")
show()


# Keep running until all tasks are completed
while tasks:
    # For each task, compute shortest path and pick the nearest one
    paths_and_goals = [(bfs(agent, t), t) for t in tasks]
    path, goal = min(
        (item for item in paths_and_goals if item[0] is not None),
        key=lambda p_g: len(p_g[0])
    )

    # Move along the path step by step (excluding starting point)
    for agent_pos in path[1:]:
        agent = agent_pos
        show()
    
    # Mark task as completed once reached
    print(f"Picked task at {goal}\n")

    # Remove task from set
    tasks.remove(goal)

# End message
print("Agent finished work")