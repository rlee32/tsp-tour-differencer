#!/usr/bin/env python3

import reader
from matplotlib import pyplot as plt

def read_tour(filename):
    tour = []
    with open(filename, 'r') as f:
        for line in f:
            tour.append(int(line))
    edges = [(min(tour[i-1], tour[i]), max(tour[i-1], tour[i])) for i in range(len(tour))]
    return edges

def difference(edges1, edges2):
    edges1 = set(edges1)
    edges2 = set(edges2)
    diff1 = []
    for edge in edges1:
        if edge not in edges2:
            diff1.append(edge)
    diff2 = []
    for edge in edges2:
        if edge not in edges1:
            diff2.append(edge)
    return diff1, diff2

def common(edges1, edges2):
    edges2 = set(edges2)
    same = []
    for edge in edges1:
        if edge in edges2:
            same.append(edge)
    return same


if __name__ == '__main__':
    problem_name = 'xqf131'
    lengths = [589, 592]
    lengths = [589, 596]
    edges1 = read_tour('solutions/{}_{}.tour'.format(problem_name, lengths[0]))
    edges2 = read_tour('solutions/{}_{}.tour'.format(problem_name, lengths[1]))
    same = common(edges1, edges2)
    xy = reader.read_xy('problems/{}.tsp'.format(problem_name))
    diff1, diff2 = difference(edges1, edges2)
    for edge in diff1:
        a = xy[edge[0]]
        b = xy[edge[1]]
        plt.plot([a[0], b[0]], [a[1], b[1]], 'x-b')
    for edge in diff2:
        a = xy[edge[0]]
        b = xy[edge[1]]
        plt.plot([a[0], b[0]], [a[1], b[1]], 'x-r')
    for edge in same:
        a = xy[edge[0]]
        b = xy[edge[1]]
        plt.plot([a[0], b[0]], [a[1], b[1]], 'k:')
    plt.show()
