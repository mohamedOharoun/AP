#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx

def solve(input_list):
    # Construcción del grafo
    graph = nx.Graph()
    for path in input_list:
        temp = path.split('-')
        graph.add_edge(temp[0], temp[1])
    
    num_solutions = 0
    all_paths = []
    lowercase_visited = set()
    current_path = list()
    special_flag = False
    special_cave = None
    
    def dfs(cave, current_path):
        nonlocal num_solutions
        nonlocal special_flag
        nonlocal special_cave
        
        if cave in lowercase_visited:
            if cave != 'start' and not special_flag:
                special_flag = True
                special_cave = cave
            else:
                return
         
        if cave == 'end':
            num_solutions += 1
            all_paths.append(current_path.copy() + ['end'])
            return
        
        current_path.append(cave)
        if cave.islower():
            lowercase_visited.add(cave)
        
        for c in graph.neighbors(cave):
            dfs(c, current_path)
        
        current_path.pop()
        
        if cave == special_cave:
            special_flag = False
            special_cave = None
        else:
            lowercase_visited.discard(cave)
    
    current_path.append('start')
    lowercase_visited.add('start')
    for cave in graph.neighbors('start'):
        dfs(cave, current_path)
    return num_solutions, all_paths

first_line = input().split()
num_lines  = int(first_line[0])

input_list = []
for j in range(num_lines):
    input_list.append(input())

num_solutions, solutions_list = solve(input_list)

# VPL output

solutions_list.sort()
solutions_list.sort(key=len)

for sublist in solutions_list:
    print(sublist)

print(num_solutions)