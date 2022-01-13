import itertools
import math

def main():
    lines = []
    with open('day13.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    graph = []
    for line in lines:
        tmp = line.split()
        A = tmp[0]
        B = tmp[-1][:-1]

        effect = tmp[2]
        weight = 0
        if effect == "gain":
            weight = int(tmp[3])
        elif effect == "lose":
            weight = int(tmp[3]) * -1

        if not nodeExists(graph, A):
            graph.append(Node(A))

        if not nodeExists(graph, B):
            graph.append(Node(B))

        NodeA = findNodeByID(graph, A)
        NodeB = findNodeByID(graph, B)

        if NodeA.edges.get(B) is None:
            NodeA.edges[B] = weight
        else:
            NodeA.edges[B] = NodeA.edges.get(B) + weight

        if NodeB.edges.get(A) is None:
            NodeB.edges[A] = weight
        else:
            NodeB.edges[A] = NodeB.edges.get(A) + weight

    routes = list(itertools.permutations(graph))
    smallestRoute = math.inf
    longestRoute = 0
    weakOfBest = None

    for route in routes:
        routeCost = 0
        weakestEdge = math.inf
        for index, node in enumerate(route):
            if index == len(route) - 1:
                routeCost += node.edges.get(route[0].ID)
                if node.edges.get(route[0].ID) < weakestEdge:
                    weakestEdge = node.edges.get(route[0].ID)
            else:
                arossNode = route[index + 1]
                routeCost += node.edges.get(arossNode.ID)
                if node.edges.get(arossNode.ID) < weakestEdge:
                    weakestEdge = node.edges.get(arossNode.ID)

        if routeCost < smallestRoute:
            smallestRoute = routeCost
        if routeCost > longestRoute:
            longestRoute = routeCost
            weakOfBest = weakestEdge

    print("Smallest route cost: " + str(smallestRoute))
    print("Longest route cost: " + str(longestRoute))
    print("Best solution if I insert myself: " + str(longestRoute - weakOfBest))

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