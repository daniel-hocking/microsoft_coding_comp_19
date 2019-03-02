from collections import defaultdict

class solution():
    vertices = defaultdict(list)
    paths = set()
    total = 0
    
    def __init__(self, vertices):
        self.vertices = vertices
    
    def paths_from_start(self, start, current, so_far, path):
        for v in self.vertices[current]:
            ends = tuple(sorted([start, v[0]]))
            if v[0] not in path:
                new_so_far = so_far + v[1]
                if not ends in self.paths:
                    self.paths.add(ends)
                    #print(ends)
                    #print(new_so_far)
                    self.total += new_so_far
                new_path = list(path) + [v[0]]
                self.paths_from_start(start, v[0], new_so_far, new_path)

    def find_paths(self):
        for v in self.vertices:
            self.paths_from_start(v, v, 0, [v])
        print(self.total)

N = int(input())
vertices = defaultdict(list)
for i in range(N - 1):
    v = tuple(map(int, input().split()))
    vertices[v[0]].append((v[1], v[2]))
    vertices[v[1]].append((v[0], v[2]))
    
sol = solution(vertices)
sol.find_paths()
