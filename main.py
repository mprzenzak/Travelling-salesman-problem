from itertools import permutations
import time


# Load matrix of path costs from txt data file
def load_graph(filename):
    datafile = open(filename, "r")
    lines = datafile.read().splitlines()
    matrix = []
    for i in range(1, len(lines)):
        matrix.append(lines[i].split())
    datafile.close()
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
    # Initialize path as list for vertices
    path = []
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
            path = list(route)
            path.insert(0, 0)
            path.append(0)
    return min_path, path


def load_initialization_file(filename):
    init_file = open(filename, "r")
    configuration = init_file.read().splitlines()
    init_file.close()
    return configuration


def test_algorithm(configuration):
    output_file = open(configuration[len(configuration) - 1], "w")
    for testing_case in range(len(configuration) - 1):
        output_file.write(configuration[testing_case] + "\n")
        testing_case_data = configuration[testing_case].split()
        file_name = testing_case_data[0]
        number_of_tests = int(testing_case_data[1])
        min_path_weight = int(testing_case_data[2])
        min_path = list(map(int, configuration[testing_case].split("[")[1].split(']')[0].split()))

        if file_name == "tsp_6_1.txt" or file_name == "tsp_6_2.txt":
            for test in range(number_of_tests):
                ten_repetitions_time = 0
                for repetition in range(20):
                    start = time.time_ns()
                    counted_min_path_weight, counted_path = find_path(load_graph("TestData/" + file_name),
                                                                      get_number_of_cities("TestData/" + file_name))
                    if counted_min_path_weight == min_path_weight:
                        print("Good job, that's right.")
                    else:
                        print("The algorithm is wrong. Check the minimal path weight.")

                    if counted_path == min_path:
                        print("Good job, that's right.")
                    else:
                        print("The algorithm is wrong. Check the minimal path")

                    end = time.time_ns()
                    ten_repetitions_time += end - start
                operation_time = ten_repetitions_time / 20
                output_file.write(str(operation_time) + "\n")
        else:
            for test in range(number_of_tests):
                operation_time = 0
                start = time.time_ns()
                counted_min_path_weight, counted_path = find_path(load_graph("TestData/" + file_name),
                                                                  get_number_of_cities("TestData/" + file_name))
                if counted_min_path_weight == min_path_weight:
                    print("Good job, that's right.")
                else:
                    print("The algorithm is wrong. Check the minimal path weight.")

                if counted_path == min_path:
                    print("Good job, that's right.")
                else:
                    print("The algorithm is wrong. Check the minimal path")

                end = time.time_ns()
                operation_time += end - start
                output_file.write(str(operation_time) + "\n")
    output_file.write(configuration[len(configuration) - 1])
    output_file.close()


if __name__ == "__main__":
    configuration = load_initialization_file("init.ini")
    test_algorithm(configuration)
