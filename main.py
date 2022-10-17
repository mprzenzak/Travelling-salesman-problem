from itertools import permutations

# Load matrix of path costs from txt data file
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


# Returns the permutation of nodes
def get_permutation(start_node, number_of_cities):
    nodes = []
    for node in range(int(number_of_cities)):
        if node != start_node:
            nodes.append(node)
    return permutations(nodes)


def find_path(data, number_of_cities):
    # Initialize min_path as maximal int size
    min_path = 2147483647
    # Assume that we always start from the first node
    options = get_permutation(0, number_of_cities)
    for route in options:
        weight = 0
        i = 0
        for vertex in route:
            weight += int(data[i][vertex])
            i = vertex
        # Assume that we always start from the first node
        weight += int(data[i][0])
        if weight < min_path:
            min_path = weight
    print(min_path)


if __name__ == "__main__":
    find_path(load_graph("data.txt"), get_number_of_cities("data.txt"))
