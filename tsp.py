import heapq

inf = 10**9

class Node:
    def __init__(self, n=0):
        self.matrix = [[inf] * n for _ in range(n)]
        self.cost = 0
        self.level = 0
        self.vertex = 0
        self.path = []

    def __lt__(self, other):
        return self.cost < other.cost


def reduce_matrix(mat):
    n = len(mat)
    reduc = 0

    for i in range(n):
        row_min = min(mat[i])
        if row_min != inf and row_min > 0:
            reduc += row_min
            for j in range(n):
                if mat[i][j] != inf:
                    mat[i][j] -= row_min

    for j in range(n):
        col_min = min(mat[i][j] for i in range(n))
        if col_min != inf and col_min > 0:
            reduc += col_min
            for i in range(n):
                if mat[i][j] != inf:
                    mat[i][j] -= col_min

    return reduc


def create_child(parent, from_city, to_city):
    n = len(parent.matrix)
    child = Node(n)
    child.matrix = [row[:] for row in parent.matrix]

    for j in range(n):
        child.matrix[from_city][j] = inf
    for i in range(n):
        child.matrix[i][to_city] = inf

    child.matrix[to_city][0] = inf

    edge_cost = parent.matrix[from_city][to_city]
    reduction_cost = reduce_matrix(child.matrix)

    child.cost = parent.cost + edge_cost + reduction_cost
    child.level = parent.level + 1
    child.vertex = to_city
    child.path = parent.path + [to_city]

    return child


def solve_tsp_lcbb(cost_matrix):
    n = len(cost_matrix)
    root = Node(n)
    root.matrix = [row[:] for row in cost_matrix]
    
    for i in range(n):
        root.matrix[i][i] = inf

    root.cost = reduce_matrix(root.matrix)
    root.path = [0]
    root.vertex = 0
    root.level = 0

    pq = []
    heapq.heappush(pq, root)

    while pq:
        curr = heapq.heappop(pq)

        if curr.level == n - 1:
            curr.path.append(0)
            return curr.cost, curr.path

        for next_city in range(n):
            if curr.matrix[curr.vertex][next_city] != inf:
                child = create_child(curr, curr.vertex, next_city)
                heapq.heappush(pq, child)

    return None, []


cost_matrix = [
    [inf, 10, 15, 20],
    [10, inf, 35, 25],
    [15, 35, inf, 30],
    [20, 25, 30, inf]
]

min_cost, optimal_path = solve_tsp_lcbb(cost_matrix)
print(f"Optimal Tour Cost: {min_cost}")
print(f"Optimal Path: {' -> '.join(map(str, optimal_path))}")
