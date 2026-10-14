import heapq


inf = 10**9


class Node:
    def __init__(self, n=0):
        self.matrix = [[inf]*n for I in range(n)]

        self.cost = 0
        self.level = 0
        self.vertex = 0
        self.path = []

def reduce_matix(mat):
    n = len(mat)
    reduc = 0

    for i in range(n):
        row_min = min(mat[i])

        if row_min != inf and row_min > 0:
            reduc+=row_min
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

def create_child(parent, fromCity, to):

    n = len(parent.matrix)
    child = Node(n)

    child.matrix = [row[:] for row in parent.matrix]

    for j in range(n):
        child.matrix[fromCity][j] = inf

    for i in range(n):
        child.matrix[i][to] = inf

    edge_cost = parent.matrix[fromCity][to]

    child.cost = parent.cost + edge
