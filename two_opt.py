#/usr/bin/env python3

import reader
from tour import Tour
import sys

class TwoOpt:
    def __init__(self, xy):
        self.tour = Tour(xy)
    def sequence(self, start = 0):
        return range(start, self.tour.n)
    def improve_once(self):
        for si in self.sequence():
            igain = self.tour.next_length(si)
            for sj in self.sequence(si + 2):
                jgain = self.tour.next_length(sj)
                cost = self.tour.length(si, sj) + self.tour.length(si + 1, sj + 1)
                improvement = igain + jgain - cost
                if improvement > 0:
                    self.tour.swap(si, sj)
                    return improvement
        return 0
    def optimize(self):
        original = self.tour.tour_length()
        improvement = self.improve_once()
        while improvement > 0:
            improvement = self.improve_once()
        optimized = self.tour.tour_length()
        improvement = original - optimized
        assert(improvement >= 0)
        return improvement

if __name__ == "__main__":
    problem_name = 'xqf131'
    xy = reader.read_xy("problems/{}.tsp".format(problem_name))
    t = TwoOpt(xy)
    t.tour.randomize()
    t.optimize()
    #t.tour.plot()
    #t.tour.show()
    final_length = t.tour.tour_length()
    t.tour.write("solutions/{}_{}.tour".format(problem_name, final_length))
    print("final length: " + str(final_length))
