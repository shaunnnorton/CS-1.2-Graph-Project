from Graph import Graph
from Vertex import Vertex
import json


def jsonToGraph(json_path):
    file = json.loads(open(json_path, 'r').read())
    new_graph = Graph()
    for course in file:
        new_vertex = Vertex(course['name'])
        new_graph.addVertex(new_vertex)
    for course in file:
        list_of_prerequisites = course['prerequisites']
        while len(list_of_prerequisites) > 0:
            first_index = 0
            second_index = 0
            while new_graph.vertices[first_index].id is not course['name']:
                first_index += 1
            print(list_of_prerequisites)
            while new_graph.vertices[second_index].id != list_of_prerequisites[0]:

                second_index += 1

            new_graph.vertices[first_index].add_neighbor(
                new_graph.vertices[second_index])
            del list_of_prerequisites[0]
    return new_graph


test = jsonToGraph("/Users/shaunnorton/dev/courses/CS1.2/Graph/test.json")
print(len(test.vertices))
print(test.print_path('FEW 2.3'))


def numPrereqs(graph, course_name):
    vertex = None
    for item in graph.vertices:
        if item.id == course_name:
            vertex = item
    if vertex == None:
        return('Item does not exist with that id.')
    next_items = list()
    if vertex.neighbors.keys():
        for items in vertex.neighbors.keys():
            next_items.append(items)

    if len(next_items) > 0:
        print(vertex.id + ' has the prerequisites ' + str(next_items))
    else:
        print(f'{course_name} has no prerequisites')


numPrereqs(test, 'CS 1.0')
