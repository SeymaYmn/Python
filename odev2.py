#!/usr/bin/python
import sys

def read (file_name):
    all_list = {}
    f= open(file_name)
    first_list = [item.strip().split(" ") for item in f]
    strip_list = {d[0]: d[1:] for d in first_list}
    f.close()
    return strip_list

file_name = sys.argv[1]
all_list = read(file_name)

def find(graph, start, end):
    frontier = [[start]]
    explored = []
    while frontier:
        short_path = min(frontier, key=len)
        node = short_path[-1]
        frontier.remove(short_path)
        if node == end:
            return short_path
        elif node not in explored:
            for adjacent in graph.get(node, []):
                new_path = list(short_path)
                new_path.append(adjacent)
                frontier.append(new_path)
            explored.append(node)

a= find (all_list,'Stefan', 'Marin')
print a
'''for start_name in all_list.keys():
    for end_name in all_list.keys():
        a = find(all_list,start_name,end_name)
        print start_name, end_name, a'''


