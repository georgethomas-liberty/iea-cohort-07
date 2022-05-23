class Life:
    def __init__(self, grid):
        self.grid = grid

    def next_geneartion(self):
        next_gen == []
        for row in self.grid:
            if all(row):
                next_gen.append(row)
            else:
                next_gen.append([False, False])

        return next_gen
