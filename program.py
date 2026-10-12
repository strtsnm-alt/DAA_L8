from collections import deque

q = deque()
N = 4
P = [10, 10, 12, 18]
W = [2, 4, 6, 9]
C = 15
U = 0

class Node:
    global U
    def __init__(self, ub, lb, profit, weight, level):
        self.ub = ub
        self.lb = lb
        self.profit = profit
        self.weight = weight
        self.level = level


def return_bounds(level, current_weight, current_profit):
    if current_weight > C:
        return float('inf'), float('inf')
    
    integer_profit = current_profit
    fractional_profit = current_profit
    weight_ub = current_weight
    weight_lb = current_weight
    
    for i in range(level, N):
        if weight_ub + W[i] <= C:
            weight_ub += W[i]
            integer_profit -= P[i]
        else:
            break
            
    for i in range(level, N):
        if weight_lb + W[i] <= C:
            weight_lb += W[i]
            fractional_profit -= P[i]
        else:
            remaining = C - weight_lb
            fractional_profit -= P[i] * (remaining / W[i])
            break
            
    return integer_profit, fractional_profit

root_ub, root_lb = return_bounds(0, 0, 0)
root = Node(level=0, weight=0, profit=0, ub=root_ub, lb=root_lb)

q.append(root)
U = root_ub

while q:
    node = q.popleft()
    if node.lb>U:
        continue
    if node.level == N:
        continue

    next_item = node.level

    ##include item
    next_w = node.weight+W[next_item]
    next_p = node.profit+P[next_item]
    if next_w <= C:
        l_ub,  l_lb = return_bounds(next_item+1, next_w, next_p)

        if l_ub < U:
            U = l_ub

        if l_lb <= U:
            left_node = Node(next_item+1, next_w, next_p, l_lb, l_ub)
            q.append(left_node)

    ##exclude item
    r_ub, r_lb = return_bounds(next_item+1, node.weight, node.profit)

    if r_ub < U:
        U = r_ub

    if r_lb <= U:
        right_node = Node(next_item+1, node.weight, node.profit, r_lb, r_ub)
        q.append(right_node)

print(f"\nMaximum Profit: {abs(U)}")


