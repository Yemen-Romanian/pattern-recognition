# Author: Stefan Haller <stefan.haller@iwr.uni-heidelberg.de>


class Grid:

    def __init__(self, nodes, edges, width, height):
        self._nodes = nodes
        self._edges = edges
        self.width = width
        self.height = height

        if True:
            for i in range(width*height):
                assert i == self.linear_index(*self.grid_index(i))

    def linear_index(self, i, j):
        assert 0 <= i < self.height
        assert 0 <= j < self.width
        return i * self.width + j

    def grid_index(self, u):
        assert 0 <= u < self.width * self.height
        index = (u // self.width, u % self.width)
        return index

    def neighbors_dict(self, u, isotropic=True):
        neighbors = {'horizontal': [], 'vertical': []}
        i, j = self.grid_index(u)

        if isotropic:
            if j > 0:
                neighbors['horizontal'].append(u - 1)

            if i > 0:
                neighbors['vertical'].append(u - self.width)

        if j + 1 < self.width:
            neighbors['horizontal'].append(u + 1)

        if i + 1 < self.height:
            neighbors['vertical'].append(u + self.width)

        return neighbors

    def neighbors(self, u, isotropic=True):
        neighbors = []
        i, j = self.grid_index(u)

        if isotropic:
            if j > 0:
                neighbors.append(u - 1)

            if i > 0:
                neighbors.append(u - self.width)

        if j + 1 < self.width:
            neighbors.append(u + 1)

        if i + 1 < self.height:
            neighbors.append(u + self.width)

        return neighbors

    def edge(self, u, v):
        assert 0 <= u < self.height * self.width
        assert v >= 0 and u < self.height*self.width
        # neighbours = self.neighbors(u, isotropic=isotropic)
        # assert v in neighbours['horizontal'] + neighbours['vertical']

        if u > v:
            u, v = v, u

        i, j = self.grid_index(u)

        idx = (2*(self.width-1) + 1) * i + 2*j

        if i == self.height - 1:
            idx -= j

        if i != self.height-1 and j != self.width-1:
            idx = idx if (u + 1 == v) else idx + 1

        edge = self._edges[idx]
        assert edge.left == u and edge.right == v
        return edge

    def edges_dict(self, u, isotropic=True):
        edges_dict = {}
        for k, vertices in self.neighbors_dict(u, isotropic=isotropic).items():
            edges_dict[k] = [self.edge(v, u) for v in vertices]

        return edges_dict

    def edges(self, u, isotropic):
        return [self.edge(u, v) for v in self.neighbors(u, isotropic=isotropic)]

def determine_grid(nodes, edges):
    i = 0
    while edges[2*i].left == i and edges[2*i].right == i+1:
        i += 1

    width = i + 1
    assert len(nodes) % width == 0
    height = len(nodes) // width

    return Grid(nodes, edges, width, height)


def row_column_decomposition(grid):
    decomposition = []

    # rows
    for i in range(grid.height):
        row = []
        for j in range(grid.width - 1):
            u = grid.linear_index(i, j)
            v = grid.linear_index(i, j+1)
            row.append(grid.edge(u, v))
        decomposition.append(row)

    # columns
    for j in range(grid.width):
        column = []
        for i in range(grid.height-1):
            u = grid.linear_index(i, j)
            v = grid.linear_index(i+1, j)
            column.append(grid.edge(u, v))
        decomposition.append(column)

    return decomposition
