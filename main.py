from itertools import permutations


def load_graph(filename):
    datafile = open(filename, "r")
    lines = datafile.read().splitlines()
    matrix = []
    for i in range(1, len(lines) - 1):
        matrix.append(lines[i].split())
    return matrix


def get_number_of_cities(filename):
    datafile = open(filename, "r")
    return datafile.readline()


def get_permutations_number(start_node, number_of_cities):
    nodes = []
    for node in range(int(number_of_cities)):
        if node != start_node:
            nodes.append(node)
    return permutations(nodes)


def find_path(data, number_of_cities):
    min_path = 2147483647
    # assume that we always start from the first node
    options = get_permutations_number(0, number_of_cities)
    for route in options:
        weight = 0
        i = 0
        for vertex in route:
            weight += int(data[i][vertex])
            i = vertex
        # assume that we always start from the first node
        weight += int(data[i][0])
        if weight < min_path:
            min_path = weight
    print(min_path)


if __name__ == "__main__":
    find_path(load_graph("data.txt"), get_number_of_cities("data.txt"))



# from sys import maxsize
# from itertools import permutations
#
# V = 4
#
#
# # implementation of traveling Salesman Problem
# def travellingSalesmanProblem(graph, s):
#     # store all vertex apart from source vertex
#     vertex = []
#     for i in range(V):
#         if i != s:
#             vertex.append(i)
#
#     # store minimum weight Hamiltonian Cycle
#     min_path = maxsize
#     next_permutation = permutations(vertex)
#     for i in next_permutation:
#
#         # store current Path weight(cost)
#         current_pathweight = 0
#
#         # compute current path weight
#         k = s
#         for j in i:
#             current_pathweight += int(graph[k][j])
#             k = j
#         current_pathweight += int(graph[k][s])
#
#         print(current_pathweight)
#         print("current_pathweight")
#         # update minimum
#         min_path = min(min_path, current_pathweight)
#
#     return min_path
#
#
# # Driver Code
# if __name__ == "__main__":
#     # matrix representation of graph
#     # graph = [[0, 10, 15, 20], [10, 0, 35, 25],
#     #          [15, 35, 0, 30], [20, 25, 30, 0]]
#     graph = load_graph("data.txt")
#     s = 0
#     print(travellingSalesmanProblem(graph, s))