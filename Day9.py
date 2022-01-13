import itertools
import math

def main():
    lines = []
    with open('day9.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    graph = []

    for line in lines:
        tmp = line.split()
        A = tmp[0]
        B = tmp[2]
        weight = int(tmp[4])

        if not nodeExists(graph, A):
            graph.append(Node(A))

        if not nodeExists(graph, B):
            graph.append(Node(B))

        NodeA = findNodeByID(graph, A)
        NodeB = findNodeByID(graph, B)

        NodeA.edges[B] = weight
        NodeB.edges[A] = weight

    routes = list(itertools.permutations(graph))
    smallestRoute = math.inf
    longestRoute = 0
    for route in routes:
        routeCost = 0
        for index, node in enumerate(route):
            if index == len(route) - 1:
                break
            arossNode = route[index + 1]
            routeCost += node.edges.get(arossNode.ID)

        print(routeCost)

        if routeCost < smallestRoute:
            smallestRoute = routeCost
        if routeCost > longestRoute:
            longestRoute = routeCost

    print("Smallest route cost: " + str(smallestRoute))
    print("Longest route cost: " + str(longestRoute))


def nodeExists(graph, ID):
    for node in graph:
        if node.ID == ID:
            return True
    return False

def findNodeByID(graph, ID):
    for node in graph:
        if node.ID == ID:
            return node

class Node:
    def __init__(self, ID):
        self.ID = ID
        self.edges = {}


if __name__ == "__main__":
    main()